import get_input as g
import globals
def add_students():


    def add_student():
        first_name = g.get_first_name()
        last_name = g.get_last_name()
        email = g.get_email()
        gender = g.get_gender()
        age = g.get_age()
        address = g.get_address()
        gpa = g.get_gpa()
        # the id from file
        globals.id += 1
        globals.students[globals.id] = {
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

    globals.added = True

    print("Student(s) added successfully !")


def search_student(id):
    if globals.students.get(id):
        print(
            f"ID:{id:<4} Name :{globals.students.get(id)['first_name']}{globals.students.get(id)['last_name']:<10}Email :{globals.students.get(id)['email']:<20}"
            f"Age :{globals.students.get(id)['age']:<7}Gpa :{globals.students.get(id)['gpa']:<6} gender :{globals.students.get(id)['gender']:<12} Address :{globals.students.get(id)['address']},gender:{globals.students.get(id)['gender']:<10}"
        )
    else:
        print("Student not found")


def view_students():
    index = 1
    if len(globals.students) != 0:
        for key, value in globals.students.items():
            # printing students and adding some foramat
            print(
                f"{index}- ID:{key:<4} Name :{value['first_name']} {value['last_name']:<10} Email :{value['email']:<30}"
                f" Age :{value['age']:<7} Gpa :{value['gpa']:<8} gender :{value['gender']:<6} Address :{value['address']}"
            )
            index += 1
    else:
        print("No students to print! ")


def update_student_details(student_id):

    print("What do you want to update ?")
    print("1 - first name")
    print("2 - last name")
    print("3 - email")
    print("4 - age")
    print("5 - gpa")
    print("6 - address")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        first_name = g.get_first_name()
        globals.students.get(student_id)["first_name"] = first_name
        print("First name successfully updated")

    elif choice == 2:
        last_name = g.get_last_name()
        globals.students.get(student_id)["last_name"] = last_name
        print("last name successfully updated")

    elif choice == 3:
        email = g.get_email()
        globals.students.get(student_id)["email"] = email
        print("Email successfully updated")

    elif choice == 4:
        age = g.get_age()
        globals.students.get(student_id)["age"] = age
        print("Age successfully updated")

    elif choice == 5:
        gpa = g.get_gpa()
        globals.students.get(student_id)["gpa"] = gpa
        print("GPA successfully updated")

    elif choice == 6:
        address = g.get_address()
        globals.students.get(student_id)["address"] = address
        print("Address successfully updated")

    elif choice == -1:
        return

    else:
        print("Invaild input , please enter correct number")

    globals.updated = True


def delete_student(id):
    if globals.students.get(id):
        globals.deleted = True
        globals.students.pop(id)
        print(f"student with ID={id} deleted")
    else:
        print("This ID not found")
