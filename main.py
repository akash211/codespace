from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    # Read students.json
    with open("students.json", "r") as f:
        students = json.load(f)
    # Create a name to marks mapping
    name_to_marks = {student["name"]: student["marks"] for student in students}
    print(f"Received names: {name}")
    print(f"Name to marks: {name_to_marks}")
    # Get marks for each name in the query
    marks = [name_to_marks.get(n, None) for n in name]
    return {"marks": marks}