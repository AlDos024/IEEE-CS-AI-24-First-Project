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
                    key_val = column.split(":")
                    data_dict[key_val[0]] = key_val[1]
                loaded_students[int(st[i])]= data_dict
    else:
        print("no data to load")
    # print(loaded_students)
        
# this should be called before starting the program to normalize the data
def get_last_id():
    global id
    if os.path.exists("tmp.txt"):
        with open("tmp.txt") as f:
            st = f.read().split()
            id = st[-2]



            
# print(students)
