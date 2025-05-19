from fastapi import FastAPI,Path
from pydantic import BaseModel

app=FastAPI()

students ={
    1: {"name": "John", "age": 20},
    2: {"name": "Jane", "age": 22},
}

class Student(BaseModel):
    name: str
    age: int
    year:str

@app.get("/")
def index():
	return {"message": "Hello World"}

@app.get("/student/{id}")
def get_student(id:int=Path(description="The ID of the student to get")):
    return students[id]

@app.post("/create-student/{student-id}")
def create_student(student_id:int ,student:Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student.dict()
    return students[student_id]