def add_students():
    student_data = {}

    def add_student():
        nonlocal student_data  # Accessing the outer scope variable
        nonlocal student_id
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        gender = input("Enter student gender: ")
        birth_date = input("Enter student birth date (YYYY-MM-DD): ")
        address = input("Enter student address: ")
        grade = float(input("Enter student grade: "))
        student_id = str(len(student_data) + 1)
        student_data[student_id] = {
            'name': name,
            'email': email,
            'gender': gender,
            'birth_date': birth_date,
            'address': address,
            'grade': grade
        }

    num_students = int(input("How many students do you want to add? "))

    for i in range(num_students):
        add_student()

    print("Students successfully added!")
    return student_data

students = add_students()


def display_students_data(students):
    for student_id, data in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Gender: {data['gender']}")
        print(f"Birth Date: {data['birth_date']}")
        print(f"Address: {data['address']}")
        print(f"Grade: {data['grade']}")
        print()



display_students_data(students)

