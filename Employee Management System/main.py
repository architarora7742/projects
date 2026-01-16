# To run this app, please install fastapi and Uviorn using pip install fastapi, pip install uvicorn in your virtual environment
# Uvicorn is the server which is used in backend
# to run the app --> uvicorn main:api --> type this command in Terminal
# http://127.0.0.1:8000/docs#/ --> go to this link
# Pydantic is used for the data validation
# Please contact me for any help

from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

import datetime


class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=512, description="Name of the employee")
    email: str = Field(..., description="Employee email id")
    department: str = Field(..., max_length=34, description="Department of the employee")
    role: str = Field(..., description="Employee Role in the company")



class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int = Field(..., description="Unique Identifier of the employee")
    date_joined: str = datetime.datetime.today().isoformat()


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=512, description="Name of the employee")
    email: Optional[str] = Field(None, description="Employee email id")
    department: Optional[str] = Field(None, max_length=34, description="Department of the employee")
    role: Optional[str] = Field(None, description="Employee Role in the company")



api = FastAPI()

EMPLOYEES = [
    Employee(
        id=1,
        name="Archit",
        email="archit@gmail.com",
        department="Engineering",
        role="Developer",
        date_joined=datetime.datetime.today().isoformat()
    ),
    Employee(
        id=2,
        name="Rohit",
        email="rohit@gmail.com",
        department="Engineering",
        role="Developer",
        date_joined=datetime.datetime.today().isoformat()
    ),
    Employee(
        id=3,
        name="Akshay",
        email="akshay@gmail.com",
        department="Sales",
        role="Manager",
        date_joined=datetime.datetime.today().isoformat()
    ),
    Employee(
        id=4,
        name="Amish",
        email="amish@gmail.com",
        department="Engineering",
        role="Developer",
        date_joined=datetime.datetime.today().isoformat()
    ),
    Employee(
        id=5,
        name="Aditya",
        email="aditya@gmail.com",
        department="HR",
        role="Analyst",
        date_joined=datetime.datetime.today().isoformat()
    )
]


@api.get("/employee/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    for employee in EMPLOYEES:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee Not Found")


@api.get("/employees", response_model=List[Employee])
def get_all_employees(first_n: int = None):
    if first_n:
        return EMPLOYEES[:first_n]

    return EMPLOYEES


@api.post("/employees")
def create_employee(employee: EmployeeCreate):
    new_employee_id = max(emp.id for emp in EMPLOYEES) + 1

    new_employee = Employee(
        id = new_employee_id,
        name =  employee.name,
        email = employee.email,
        department = employee.department,
        role =  employee.role,
        date_joined = datetime.datetime.today().isoformat()
    )
    EMPLOYEES.append(new_employee)
    return new_employee


@api.patch("/employee/{employee_id}", response_model=EmployeeUpdate)
def update_employee(employee_id: int, updated_employee: EmployeeUpdate):
    for emp in EMPLOYEES:
        if emp.id == employee_id:
            if updated_employee.name is not None:
                emp.name = updated_employee.name
            if updated_employee.email is not None:
                emp.email = updated_employee.email
            if updated_employee.department is not None:
                emp.department = updated_employee.department
            if updated_employee.role is not None:
                emp.role = updated_employee.role

            return emp   # ✅ return FULL Employee

    raise HTTPException(status_code=404, detail="Employee Not Found")




@api.delete("/employee/{employee_id}", response_model=Employee)
def delete_employee(employee_id: int):
    for index, emp in enumerate(EMPLOYEES):
        if emp.id == employee_id:
            return EMPLOYEES.pop(index)

    raise HTTPException(status_code=404, detail="Employee Not Found")

