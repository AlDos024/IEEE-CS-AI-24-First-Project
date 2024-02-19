import json

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
    with open("tmp.json") as f:
        students = json.load(f)
    id = list(students.keys())[-1]


load()
print(students)
