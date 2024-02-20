import os

# Note: change path(name of file).
id = 0
last_loaded_id = 0
loaded_students = {}
students = {
    "4": {"name": "a", "age": 19, "grade": "C"},
    "5": {"name": "H", "age": 20, "grade": "B"},
    "6": {"name": "A", "age": 20, "grade": "B+"},
}


def save():
    if not os.path.exists('tmp.txt'):
        with open("tmp.txt", "w") as f:
            for key, value in students.items():
                f.write(str(key) + "\n")
                f.write(f"name:{value['name']},age:{value['age']},grade:{value['grade']}\n")
    else:
         with open("tmp.txt", "a") as f:
            for key, value in students.items():
                f.write(str(key) + "\n")
                f.write(f"name:{value['name']},age:{value['age']},grade:{value['grade']}\n")



def load():
    global students
    global id
    # check if any data in saved
    if os.path.exists("tmp.txt"):
        with open("tmp.txt") as f:
            st = f.read().split()
            for i in range(0, len(st), 2):
                data_dict = {}
                data = st[i + 1].split(",")
                for column in data:
                    key, value = column.split(":")
                    data_dict[key] = value
                    
                # if student in our database then overwrite
                if not students.get(int(st[i])):
                    students.get(int(st[i])).update(data_dict)

                else:
                    students[int(st[i])] = data_dict
    else:
        print("no data to load")


# this should be called before starting the program to normalize the data
def get_last_id():
    global id
    global last_loaded_id
    if os.path.exists("tmp.txt"):
        with open("tmp.txt") as f:
            st = f.read().split()
            # assign id to last id in text file
            id = st[-2]
            last_loaded_id = st[-2]

def view_students():
    index = 0
    for key,value in students.items():
        # printing students and ding some foramat
        print(f"{index + 1}- ID:{key:<5} Name:{value['name']:<10}"
                f"Age:{value['age']:<5},Gpa:{value['gpa']:<5},Address:{value['address']},Email:{value['email']}")
        index+=1
    else:
        print("No students to print! ")