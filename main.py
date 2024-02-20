import os
# Note: change path(name of file).
id = 0
last_loaded_id = 0
loaded_students = {}
students = {
    1: {"first_name": "Amr",   "last_name":"ali","email":"amr@gmail.com",    "age": 19, "gpa": 3.79,"address":"Cairo"},
    2: {"first_name": "Hossam","last_name":"ali","email":"ali@gmail.com",    "age": 20, "gpa": 2.5 ,"address":"Tokyo"},
    3: {"first_name": "Ali",   "last_name":"ali","email":"hossam@gmail.com", "age": 20, "gpa": 3.07,"address":"madrid"},
}

def view_students():
    index = 0
    if len(students) != 0:
        for key,value in students.items():
        # printing students and ding some foramat
            print(f"{index + 1}- ID:{key:<4} Name :{value['first_name']} {value['last_name']:<10} Email :{value['email']:<30}"
                f"Age :{value['age']:<7}Gpa :{value['gpa']:<8}Address :{value['address']}")
            index+=1     
    else:
        print("No students to print! ")

def search_student(id):
    if students.get(id) != None :
         print(f"ID:{id:<4} Name :{students.get(id)['name']:<10}Email :{students.get(id)['email']:<30}"
                f"Age :{students.get(id)['age']:<7}Gpa :{students.get(id)['gpa']:<8}Address :{students.get(id)['address']}")
    else:
        print("No id") 
        

def update_student_details(student_id):
    print('What do you want to update ?')
    print('1 - first name')
    print('2 - last name')
    print('3 - email')
    print('4 - age')
    print('5 - gpa')
    print('6 - address')
    choice = int(input("Enter your choice:"))
    if choice == 1:
        first_name = input("Enter student first name: ")
        students[student_id]= {'first_name':first_name}

    elif choice == 2:
        last_name = input("Enter student last name: ")
        students[student_id]= {'last_name':last_name}

    elif choice == 3:
        email = input("Enter student email : ")
        students[student_id]= {'email':email}

    elif choice == 4:
        age = input("Enter student age : ")
        students[student_id]= {'age':age}

    elif choice == 5:
        gpa = input("Enter student gpa : ")
        students[student_id]= {'gpa':gpa}
    
    elif choice == 6:
        address = input("Enter student address: ")
        students[student_id]= {'address':address}
    
  


def delete_student(id):
    
    if students.get(id) != None :
        print(f"student with ID={id} deleted")
        students.pop(id)
    else:
        print("This ID not found")


def save():
    with open("tmp.txt", "w") as f:
        for key ,value in students.items():
            f.write(str(key)+"\n")
            f.write(f"name:{value['name']},email:{value['email']},age:{value['age']},gpa:{value['gpa']},address:{value['address']}\n")
        f.close()

            
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
                students[int(st[i])] = data_dict
            f.close()
    else:
        print("no data to load")


        
# this should be called before starting the program to normalize the data
def get_last_id():
    global id
    global last_loaded_id
    if os.path.exists("tmp.txt"):
        with open("tmp.txt") as f:
            st = f.read().split()
            id = st[-2]
            last_loaded_id = st[-2]


get_last_id()
while True:
    print("Welcome to Student Database Management System")
    print("What do you want to do? ")
    print("1 - Add Student ")
    print("2 - View Students")
    print("3 - Search Student ")
    print("4 - Update Student Details")
    print("5 - Delete Student")
    print("6 - Save to File ")
    print("7 - Load from File")
    print("press (-1) to Exit")

    try:
        choice = int(input("Enter your choice:"))
        if choice == -1:
            break

        elif choice == 2:
            print("------------------------------------")
            view_students()
            print("------------------------------------")
    
        elif choice == 3:
            id = int(input("Enter the ID you want to Search about:"))
            search_student(id)

        elif choice == 4:
            student_id = int(input("Enter student ID to update details: "))
            if students.get(student_id) != None :
                update_student_details(student_id)
                print('Student details updated successfully.')
            else:
                print("Student not found.")
        
        elif choice == 5:
            your_id = int(input("Enter id you want to delete?"))
            delete_student(your_id)

        elif choice == 6:
            save()

        elif choice == 7:
            load()
 
        else:
            print("you input is wrong!!")
    except ValueError:
        print("you input is wrong!!")

