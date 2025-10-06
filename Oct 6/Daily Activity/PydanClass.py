from pydantic import BaseModel
class Student(BaseModel):
    name : str
    age : int
    email : str
    is_active:bool = True


data = {"name": "Aisha", "age": 21, "email": "aisha123@gmail.com"}
student = Student(**data)

print(student)
print(student.name)