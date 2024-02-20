import json
import os

id = 0
loaded_students = {}
students = {
    "1": {"name": "Amr", "age": 19, "grade": "C"},
    "2": {"name": "Hossam", "age": 20, "grade": "B"},
    "3": {"name": "Ali", "age": 20, "grade": "B+"},
}


def save():
    with open("tmp.txt", "w") as f:
        # note: ids are stored as strings not integers
        for key ,value in students.items():
            f.write(str(key)+"\n")
            f.write(f"name:{value['name']},age:{value['age']},grade:{value['grade']}\n")

            

def load():
    global loaded_students
    global id
    # check if any data in saved
    if os.path.exists("tmp.txt"):
        with open("tmp.txt") as f:
            st = f.read().split()
            for i in range(0,len(st),2):
                data_dict = {}
                data = st[i+1].split(',')
                for column in data:
                    # print(column.split(":"))
                    for key , value in column.split(":"):
                        data_dict[key] = value
                loaded_students[st[i]]= data_dict
        print(loaded_students)

            
save()
load()
# print(students)
