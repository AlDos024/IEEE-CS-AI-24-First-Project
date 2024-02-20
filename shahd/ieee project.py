
def add_students():
    student_data = {}

    def add_student():
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        gender = input("Enter student gender: ")
        birth_date = input("Enter student birth date (YYYY-MM-DD): ")
        address = input("Enter student address: ")
        grade = float(input("Enter student grade: "))
        return [name, email, gender, birth_date, address, grade]

    num_students = int(input("How many students do you want to add? "))

    for i in range(num_students):
        while True:
            student_id = input("Enter student ID: ")
            if student_id not in student_data:
                break
            else:
                print("ID already exists. Please enter a different ID.")

        student_data[student_id] = add_student()

    print("Students successfully added!")
    return student_data


def display_student_data(students):
    print("\nStudent data:")
    for student_id, data in students.items():
        print("ID:", student_id)
        print("Name:", data[0])
        print("Email:", data[1])
        print("Gender:", data[2])
        print("Birth Date:", data[3])
        print("Address:", data[4])
        print("Grade:", data[5])
        print()



students = add_students()


display_student_data(students)


def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        print("The student deleted successfully.")
    else:
        print("Student with ID", student_id, "not found.")


# Call the delete_student_by_id function to delete a student by ID
delete_student_id = input("Enter the ID of the student you want to delete: ")
delete_student(students, delete_student_id)

# Display the updated student data
display_student_data(students)

