from fastapi.testclient import TestClient
from employee_api import app

client = TestClient(app)

def test_get_all_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_employee():
    new_employee = {
        "id":3,
        "name":"Neha Sharma",
        "department":"IT",
        "salary":600000
    }
    response = client.post("/employees", json=new_employee)
    assert response.status_code == 201
    assert response.json()["name"]=="Neha Sharma"

def test_get_employee_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Ravi Kumar"

def test_employee_not_found():
    response = client.get("/employees/99")
    assert response.status_code == 404
    assert response.json()["detail"]=="Employee not found"

def test_put_employee_by_id():
    new_employee = {
        "id": 1,
        "name": "Ravi Kumar",
        "department": "IT",
        "salary": 600000
    }
    response = client.put("/employees/1",json=new_employee)
    assert response.status_code == 200
    assert response.json()["salary"] == 600000


def test_delete_employee_by_id():
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Ravi Kumar"



