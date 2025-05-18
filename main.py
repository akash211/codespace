from fastapi import FastAPI, Query
from typing import List
import json
import os

app = FastAPI()

# Load data from JSON file
def read_json_file():
    file_path = os.path.join(os.getcwd(), "students.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/api")
def get_student_marks(name: List[str] = Query(default=[])):
    try:
        data = read_json_file()

        # Case-insensitive match and extract marks
        marks = [
            student["marks"]
            for student in data
            if any(student["name"].lower() == n.lower() for n in name)
        ]

        return {"marks": marks}
    except Exception as e:
        return {"error": f"Failed to process request: {str(e)}"}
