import crud
import files
import globals

files.get_last_id()

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
            crud.add_students()

        elif choice == 2:
            print("------------------------------------")
            crud.view_students()
            print("------------------------------------")

        elif choice == 3:

            id = int(input("Enter the ID you want to Search about: "))
            crud.search_student(id)

        elif choice == 4:
            student_id = int(input("Enter student ID to update details: "))
            if globals.students.get(student_id):
                crud.update_student_details(student_id)
                print("Student details updated successfully.")
            else:
                print("Student not found.")

        elif choice == 5:

            your_id = int(input("Enter id you want to delete? "))

            crud.delete_student(your_id)

        elif choice == 6:
            files.save()

        elif choice == 7:
            files.load()

        else:
            print("you input is wrong!!")

    except ValueError:
        print("you input is wrong!!")
