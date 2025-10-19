from fastapi import FastAPI, HTTPException,Request,BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import pymysql
from fastapi.responses import JSONResponse
import logging
import time
import traceback
import pandas as pd
from etl import run_etl
import pika
from Analytics import generate_student_insights
import json

app = FastAPI()

logging.basicConfig(
    filename="app.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    try:
        response = await call_next(request)
    except Exception as e:
        #duration = round(time.time() - start, 3)
        logging.error(
            f"Exception in {request.method} {request.url.path}: {str(e)}\n{traceback.format_exc()}"
        )
        raise e
    duration = round(time.time() - start, 3)
    logging.info(
        f"{request.method} {request.url.path} | Status: {response.status_code} | Duration: {duration}s"
    )
    return response

# Path to frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), "frontend")

# Mount frontend static files under /frontend
app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

# Serve index.html at root
@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open(os.path.join(frontend_path, "index.html"), "r", encoding="utf-8") as f:
        logging.info("Frontend loaded")
        return f.read()

# Allow frontend JS to call APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can restrict to ["http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    StudentID: int
    Name: str
    Age: int
    Course: str

# MySQL connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="student_pipline",
        cursorclass=pymysql.cursors.DictCursor
    )

# conn = get_connection()
@app.get("/students")
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    stud = cursor.fetchall()
    logging.info("Get Students")
    conn.close()
    return stud

@app.post("/students", status_code=201)
def add_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (StudentID, Name, Age, Course) VALUES (%s, %s, %s, %s)",
                       (student.StudentID, student.Name, student.Age, student.Course))
        conn.commit()
        logging.info("New Student Added")
    except pymysql.err.IntegrityError:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    finally:
        conn.close()
    return {"message": "Student added successfully"}

# PUT /students/{id}
@app.put("/students/{id}")
def update_student(id: int, student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET Name=%s, Age=%s, Course=%s WHERE StudentID=%s",
                   (student.Name, student.Age, student.Course, id))
    conn.commit()
    logging.info(f"Student Record for {id} Updated")
    conn.close()
    return {"message": "Student updated successfully"}

# DELETE /students/{id}
@app.delete("/students/{id}")
def delete_student(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE StudentID=%s", (id,))
    conn.commit()
    logging.info(f"Student Record for {id} Deleted")
    conn.close()
    return {"message": "Student deleted successfully"}

@app.post("/process-etl")
def process_etl():
    try:
        # Step 1: Producer — send task to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        channel = connection.channel()
        channel.queue_declare(queue="etl_tasks", durable=True)

        csv_path = "data/marks.csv"
        message = json.dumps({"csv_path": csv_path})
        channel.basic_publish(
            exchange="",
            routing_key="etl_tasks",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )
        connection.close()
        logging.info(f"Producer: Task queued for {csv_path}")

        # Step 2: Consumer — fetch and process task immediately
        def consume_once():
            connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
            channel = connection.channel()
            channel.queue_declare(queue="etl_tasks", durable=True)

            method_frame, header_frame, body = channel.basic_get(queue="etl_tasks", auto_ack=False)
            if method_frame:
                task = json.loads(body)
                logging.info(f"Consumer: Processing {task['csv_path']}")
                try:
                    start = time.time()
                    run_etl(task['csv_path'])
                    end = time.time()
                    logging.info(f"Consumer: ETL finished in {end - start:.2f} seconds")

                    df = pd.read_csv(csv_path)
                    conn = get_connection()
                    cursor = conn.cursor()

                    for _, row in df.iterrows():
                        cursor.execute("""
                                        INSERT INTO marks (StudentID, Maths, Python, ML)
                                        VALUES (%s, %s, %s, %s)
                                    """, (row["StudentID"], row["Maths"], row["Python"], row["ML"]))

                    conn.commit()
                    logging.info(f"Marks Table Updated in database")
                    conn.close()
                    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
                except Exception as e:
                    logging.error(f"Consumer: Error → {e}")
                    channel.basic_nack(delivery_tag=method_frame.delivery_tag)
            else:
                logging.warning("Consumer: No task found in queue")
            connection.close()

        consume_once()
        return JSONResponse(content={"message": "ETL task processed successfully"})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/generate-analytics")
def generate_analytics():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    stud = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()

    # Convert to DataFrame
    df = pd.DataFrame(stud, columns=columns)
    res = generate_student_insights(df)

    # Optional: return as JSON
    return JSONResponse(content={
        "message": res,
    })