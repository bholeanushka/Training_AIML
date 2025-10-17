from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password123!",
        database="student_db"
    )

# Pydantic model
class Student(BaseModel):
    StudentID: int
    Name: str
    Age: int
    Course: str

# app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
#
# @app.get("/", response_class=HTMLResponse)
# def serve_frontend():
#     with open("frontend/index.html", "r") as f:
#         return f.read()

# GET /students
@app.get("/students", response_model=List[Student])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.close()
    return results

# POST /students
@app.post("/students")
def add_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (StudentID, Name, Age, Course) VALUES (%s, %s, %s, %s)",
                       (student.StudentID, student.Name, student.Age, student.Course))
        conn.commit()
    except mysql.connector.IntegrityError:
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
    conn.close()
    return {"message": "Student updated successfully"}

# DELETE /students/{id}
@app.delete("/students/{id}")
def delete_student(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE StudentID=%s", (id,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}
