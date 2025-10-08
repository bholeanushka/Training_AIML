from fastapi.testclient import TestClient
from course_api import app, Course

client = TestClient(app)

def test_add_course():
    new_course = {
        "id": 5,
        "title": "Java Advanced",
        "duration": 30,
        "fee": 2000,
        "is_active":False
    }
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 201
    assert response.json()['title'] == "Java Advanced"

def test_add_duplicate_course():
    new_course = {
        "id": 5,
        "title": "Java Advanced",
        "duration": 30,
        "fee": 2000,
        "is_active":False
    }
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 400
    assert response.json()['detail'] == "Course ID already exists"

def test_add_invalid_course():
    new_course = { "id": 2, "title": "Artificial Intelligence", "duration": 0, "fee": -500, "is_active": True }
    response = client.post("/courses/",json=new_course)
    assert response.status_code == 422
    assert response.json()['detail'] == "Errors for duration and fee"

def test_courses():
    response = client.get("/courses")
    data = response.json()
    assert isinstance(data, list)
    assert all("title" and "id" and "duration" and"fee"and"is_active" in course for course in data)