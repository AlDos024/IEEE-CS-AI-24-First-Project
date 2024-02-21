import os

id = 0
students = {}
loaded = False
added = False
updated = False
deleted = False


# to not face errors in saving and loading
def removeChars(element):
    element = element.replace("/", "")
    element = element.replace(";", "")
    element = element.replace(":", "")
    return element


def get_first_name():
    while True:
        first_name = input("Enter student first name: ")
        if first_name.isalpha():
            first_name = first_name.capitalize()
            return first_name
        print("Invalid input")


def get_last_name():
    while True:
        last_name = input("Enter student last name: ")
        if last_name.isalpha():
            last_name = last_name.capitalize()
            return last_name
        print("Invalid input")


def get_email():
    while True:
        email = input("Enter student email: ")
        if email.strip() and "@" in email:
            email = removeChars(email)
            email = email.replace(" ", "")
            if email:
                return email
        print("Invalid email address format.")


def get_gender():
    while True:
        gender = input("Enter student gender (Male/Female): ").lower()
        if gender in ["male", "female"]:
            return gender
        print("Gender must be either 'Male' or 'Female'.")


def get_age():
    while True:
        try:
            age = int(input("Enter student age as an integer from 6 to 100: "))
            if 6 <= age <= 100:
                return age
            print("Invalid input. Please enter a value between 6 and 100.")
        except ValueError:
            print("Invalid input")


def get_address():
    address = input("Enter student address: ")
    address = removeChars(address)
    while not address.strip():
        print("Address cannot be empty.")
        address = input("Enter student address: ")
    return address


def get_gpa():
    while True:
        try:
            gpa = float(input("Enter student gpa: "))
            if 0 <= gpa <= 4:
                return gpa
            print("Invalid input. Please enter a value between 0 and 4.")
        except ValueError:
            print("Invalid input.")


def add_students():

    global added

    def add_student():
        first_name = get_first_name()
        last_name = get_last_name()
        email = get_email()
        gender = get_gender()
        age = get_age()
        address = get_address()
        gpa = get_gpa()
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
            if int(num_students) > -1:
                num_students = int(num_students)
                break
        else:
            print("Invalid input...enter a digit")

    for _ in range(num_students):
        add_student()

    added = True

    print("Student(s) added successfully !")


def search_student(id):
    if students.get(id):
        print(
            f"ID:{id:<4} Name :{students.get(id)['first_name']}{students.get(id)['last_name']:<10}Email :{students.get(id)['email']:<20}"
            f"Age :{students.get(id)['age']:<7}Gpa :{students.get(id)['gpa']:<6} gender :{students.get(id)['gender']:<12} Address :{students.get(id)['address']},gender:{students.get(id)['gender']:<10}"
        )
    else:
        print("Student not found")


def view_students():
    index = 1
    if len(students) != 0:
        for key, value in students.items():
            # printing students and adding some foramat
            print(
                f"{index}- ID:{key:<4} Name :{value['first_name']} {value['last_name']:<10} Email :{value['email']:<30}"
                f" Age :{value['age']:<7} Gpa :{value['gpa']:<8} gender :{value['gender']:<6} Address :{value['address']}"
            )
            index += 1
    else:
        print("No students to print! ")


def update_student_details(student_id):
    global students
    global updated
    print("What do you want to update ?")
    print("1 - first name")
    print("2 - last name")
    print("3 - email")
    print("4 - age")
    print("5 - gpa")
    print("6 - address")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        first_name = get_first_name()
        students.get(student_id)["first_name"] = first_name
        print("First name successfully updated")

    elif choice == 2:
        last_name = get_last_name()
        students.get(student_id)["last_name"] = last_name
        print("last name successfully updated")

    elif choice == 3:
        email = get_email()
        students.get(student_id)["email"] = email
        print("Email successfully updated")

    elif choice == 4:
        age = get_age()
        students.get(student_id)["age"] = age
        print("Age successfully updated")

    elif choice == 5:
        gpa = get_gpa()
        students.get(student_id)["gpa"] = gpa
        print("GPA successfully updated")

    elif choice == 6:
        address = get_address()
        students.get(student_id)["address"] = address
        print("Address successfully updated")

    elif choice == -1:
        return

    else:
        print("Invaild input , please enter correct number")

    updated = True


def delete_student(id):
    global students
    global deleted
    if students.get(id):
        deleted = True
        students.pop(id)
        print(f"student with ID={id} deleted")
    else:
        print("This ID not found")


def save():
    global loaded
    # if we did load the data and data was changed
    if loaded and (added or updated or deleted):
        # overwrite file
        with open("database.txt", "w") as f:
            for key, value in students.items():
                f.write(str(key) + "/\n")
                f.write(
                    f"first_name:{value['first_name']};last_name:{value['last_name']};email:{value['email']};gender:{value['gender']};age:{value['age']};address:{value['address']};gpa:{value['gpa']}/\n"
                )

    else:
        # append if only new data worked on
        with open("database.txt", "a") as f:
            for key, value in students.items():
                f.write(str(key) + "/\n")
                f.write(
                    f"first_name:{value['first_name']};last_name:{value['last_name']};email:{value['email']};gender:{value['gender']};age:{value['age']};address:{value['address']};gpa:{value['gpa']}/\n"
                )
    print("------- Your changes are saved! -------")


def load():
    global students
    global loaded
    global added
    loaded = True
    # check if any data is saved
    if os.path.exists("database.txt"):
        with open("database.txt") as f:
            st = f.read().strip("/")
            st = st.split("/")

            for i in range(0, len(st) - 1, 2):
                data_dict = {}
                data = st[i + 1].split(";")

                for column in data:
                    key, value = column.split(":")
                    data_dict[key.strip("\n")] = value.strip("\n")

                students[int(st[i])] = data_dict

        if added:
            # sort the dictionary after loading to avoid future bugs
            keys = list(students.keys())
            keys.sort()
            students = {key: students[key] for key in keys}
            print("---------- Data sucessfully loaded! ----------")

    else:
        print("--------------- No data to load ---------------")


# this should be called before starting the program to normalize the data
def get_last_id():
    global id
    if os.path.exists("database.txt"):
        with open("database.txt") as f:
            st = f.read().strip()
            if st:
                st = st.split("/")
                id = int(st[-3])


get_last_id()

while True:
    print("\n<-------- Welcome to Student Database Management System -------->")
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
        choice = int(input("Enter your choice: "))

        if choice == -1:
            break

        elif choice == 1:
            add_students()

        elif choice == 2:
            print("------------------------------------")
            view_students()
            print("------------------------------------")

        elif choice == 3:

            id = int(input("Enter the ID you want to Search about: "))
            search_student(id)

        elif choice == 4:
            student_id = int(input("Enter student ID to update details: "))
            if students.get(student_id):
                update_student_details(student_id)
                print("Student details updated successfully.")
            else:
                print("Student not found.")

        elif choice == 5:

            your_id = int(input("Enter id you want to delete? "))

            delete_student(your_id)

        elif choice == 6:
            save()

        elif choice == 7:
            load()

        else:
            print("you input is wrong!!")

    except ValueError:
        print("you input is wrong!!")
