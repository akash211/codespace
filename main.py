from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: list[str] = []):
    # Read students.json
    with open("students.json", "r") as f:
        students = json.load(f)
    # Create a name to marks mapping
    name_to_marks = {student["name"]: student["marks"] for student in students}
    print(name_to_marks)
    # Get marks for each name in the query
    marks = [name_to_marks.get(n, None) for n in name]
    return {"marks": name_to_marks}