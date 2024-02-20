import json
import os
id = 0

students = {
    id + 1: {"name": "Amr", "age": 19, "grade": "C"},
    id + 2: {"name": "Hossam", "age": 20, "grade": "B"},
    id + 3: {"name": "Ali", "age": 20, "grade": "B+"},
}


def save():
    with open("tmp.json", "w") as f:
        # note: ids are stored as strings not integers
        json.dump(students, f)


def load():
    global students
    global id
    if os.path.exists('tmp.json'):
        with open("tmp.json") as f:
            # check if there is data in file
            try:
                students = json.load(f)
                id = list(students.keys())[-1]
            except Exception:
                print("Nothing to load")
                
    else:
        print("Nothing to load ...")


load()
print(students)
