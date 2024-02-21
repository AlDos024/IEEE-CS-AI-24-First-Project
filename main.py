import os

id = 0
students = {}


def add_students():

    def add_student():
        while True:
            first_name = input("Enter student first name: ")
            if first_name.isalpha():
                break
            print("Invalid input")

        while True:
            last_name = input("Enter student last name: ")
            if last_name.isalpha():
                break
            print("Invalid input")

        while True:
            email = input("Enter student email: ")
            if email.strip() and "@" in email:
                break
            print("Invalid email address format.")

        while True:
            gender = input("Enter student gender (Male/Female): ").lower()
            if gender in ["male", "female"]:
                break
            print("Gender must be either 'Male' or 'Female'.")

        while True:
            try:
                age = int(input("Enter student age as an integer from 6 to 100: "))
                if 6 <= age <= 100:
                    break
                print("Invalid input. Please enter a value between 6 and 100.")
            except ValueError:
                print("Invalid input")

        address = input("Enter student address: ")
        while not address.strip():
            print("Address cannot be empty.")
            address = input("Enter student address: ")

        while True:
            try:
                gpa = float(input("Enter student gpa: "))
                if 0 <= gpa <= 4:
                    break
                print("Invalid input. Please enter a value between 0 and 4.")
            except ValueError:
                print("Invalid input.")

        # the id from file
        global id
        global students
        id += 1
        students[id] = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": gender,
            "age": age,
            "address": address,
            "gpa": gpa,
        }

    while True:
        num_students = input("How many students do you want to add? ")
        if num_students.isdigit():
            if int(num_students) > 0:
                num_students = int(num_students)
                break
        else:
            print("Invalid input...enter a digit")

    for _ in range(num_students):
        add_student()

    print("Students successfully added!")


def view_students():
    index = 0
    if len(students) != 0:
        for key, value in students.items():
            # printing students and ding some foramat
            print(
                f"{index + 1}- ID:{key:<4} Name :{value['first_name']} {value['last_name']:<10} Email :{value['email']:<30}"
                f"Age :{value['age']:<7}Gpa :{value['gpa']:<8}Address :{value['address']}"
            )
            index += 1
    else:
        print("No students to print! ")


def search_student(id):
    if students.get(id) != None:
        print(
            f"ID:{id:<4} Name :{students.get(id)['first_name']}{students.get(id)['last_name']:<10}Email :{students.get(id)['email']:<30}"
            f"Age :{students.get(id)['age']:<7}Gpa :{students.get(id)['gpa']:<8}Address :{students.get(id)['address']},gender:{students.get(id)['gender']:<10}"
        )
    else:
        print("No id")


def update_student_details(student_id):
    print("What do you want to update ?")
    print("1 - first name")
    print("2 - last name")
    print("3 - email")
    print("4 - age")
    print("5 - gpa")
    print("6 - address")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        first_name = input("Enter student first name: ")
        students[student_id] = {
            "first_name": first_name,
            "last_name": students.get(id)["last_name"],
            "email": students.get(id)["email"],
            "gender": students.get(id)["gender"],
            "age": students.get(id)["age"],
            "address": students.get(id)["address"],
            "gpa": students.get(id)["gpa"],
        }

    elif choice == 2:
        last_name = input("Enter student last name: ")
        students[student_id] = {"last_name": last_name}

    elif choice == 3:
        email = input("Enter student email : ")
        students[student_id] = {"email": email}

    elif choice == 4:
        age = input("Enter student age : ")
        students[student_id] = {"age": age}

    elif choice == 5:
        gpa = input("Enter student gpa : ")
        students[student_id] = {"gpa": gpa}

    elif choice == 6:
        address = input("Enter student address: ")
        students[student_id] = {"address": address}


def delete_student(id):

    if students.get(id) != None:
        students.pop(id)
        print(f"student with ID={id} deleted")
    else:
        print("This ID not found")


def save():
    with open("database.txt", "w") as f:
        for key, value in students.items():
            f.write(str(key) + "\n")
            f.write(
                f"first_name:{value['first_name']},last_name:{value['last_name']},email:{value['email']},gender:{value['gender']},age:{value['age']},address:{value['address']},gpa:{value['gpa']}\n"
            )
        f.close()


def load():
    global students
    global id
    # check if any data in saved
    if os.path.exists("database.txt"):
        with open("database.txt") as f:
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
    if os.path.exists("database.txt"):
        with open("database.txt") as f:
            st = f.read().split()
            if st:
                id = int(st[-2])
                last_loaded_id = int(st[-2])


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

        elif choice == 1:
            add_students()

        elif choice == 2:
            print("------------------------------------")
            view_students()
            print("------------------------------------")

        elif choice == 3:
            id = int(input("Enter the ID you want to Search about:"))
            search_student(id)

        elif choice == 4:
            student_id = int(input("Enter student ID to update details: "))
            if students.get(student_id) != None:
                update_student_details(student_id)
                print("Student details updated successfully.")
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
