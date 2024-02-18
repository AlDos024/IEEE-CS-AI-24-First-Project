students = [
    {'name': 'John', 'age': 18, 'grade': 'A', 'id': 1},
    {'name': 'Emma', 'age': 17, 'grade': 'B', 'id': 2},
    {'name': 'Michael', 'age': 16, 'grade': 'C', 'id': 3}
]

def view_students():
    if len(students) != 0:
        for student in students:
            # printing students and ding some foramat
            print(f"{students.index(student) + 1}- Name:{student['name']:<10}"
                  f"Age:{student['age']:<5}Grade:{student['grade']:<5}ID:{student['id']:<5}")
    else:
        print("No students to print! ")


# the update is not working yet
def update_student_details(name, student_id, grade, age):
    students[student_id] = {   
            'name': name,
            'id': student_id,
            'grade': grade,
            'age': age,
        }
    print('Student details updated successfully.')

def delete_student(id):
    found = False
    for student in students:
        if student['id'] == id:
            found = True
            print(f"student with ID={id} deleted")
            students.remove(student)
            break
    if not found:
        print("This ID not found")


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

        elif choice == 4:
            student_id = int(input("Enter student ID to update details: "))
            for student in students:    
                if student['id'] in student_id :
                    name = input("Enter student name: ")
                    grade = input("Enter student grade: ")
                    age = int(input("Enter student age: "))
                    update_student_details(name, student_id, grade, age)
                    print("Student details updated successfully.")
                else:
                    print("Student not found.")
        
        elif choice == 5:
            your_id = int(input("Enter id you want to delete?"))
            delete_student(your_id)
        else:
            print("you input is wrong!!")
    except ValueError:
        print(" you input is wrong!!")

