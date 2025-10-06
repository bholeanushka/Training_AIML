import json
import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')
Student = [
    {"name": "Rahul", "age": 21, "course": "AI", "marks": 85},
    {"name": "Priya", "age": 22, "course": "ML", "marks": 90}
]
# Step 1: Read and print all student names
try:
    with open("Student.json", "w") as f:
        json.dump(Student, f, indent=4)
        logging.info("File Created")
except Exception as e:
    logging.error(f"Error reading file: {e}")

with open("Student.json", "r") as f:
    data = json.load(f)
    logging.info("File read")
    print(data)

# Step 2: Add a new student
new_student = {"name": "Arjun", "age": 20, "course": "Data Science", "marks": 78}
logging.info("Student added")

# Step 3: Save the updated list back to the same JSON file
try:
    with open('Student.json', 'w') as file:
        data.append(new_student)
        json.dump(data, file, indent=4)
        logging.info("File saved")
except Exception as e:
    logging.error(f"Error saving file: {e}")

with open("Student.json", "r") as f:
    data = json.load(f)
    logging.info("File read")
    print(data)
