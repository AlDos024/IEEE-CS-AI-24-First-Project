def add_students():
    student_data = {}

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
            if email.strip() and '@' in email:
                break
            print("Invalid email address format.")

        while True:
            gender = input("Enter student gender (Male/Female): ").lower()
            if gender in ['male', 'female']:
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
                gpa = float(input("Enter student grade: "))
                if 0 <= gpa <= 4:
                    break
                print("Invalid input. Please enter a value between 0 and 4.")
            except ValueError:
                print("Invalid input.")

        nonlocal student_data
        student_id = str(len(student_data) + 1)
        student_data[student_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'gender': gender,
            'age': age,
            'address': address,
            'gpa': gpa
        }

    num_students = int(input("How many students do you want to add? "))

    for _ in range(num_students):
        add_student()

    print("Students successfully added!")
    return student_data

def display_students_data(students):
    for student_id, data in students.items():
        print(f"Student ID: {student_id}")
        print(f"First Name: {data['first_name']}")
        print(f"Last Name: {data['last_name']}")
        print(f"Email: {data['email']}")
        print(f"Gender: {data['gender']}")
        print(f"Age: {data['age']}")
        print(f"Address: {data['address']}")
        print(f"GPA: {data['gpa']}")
        print()


students = add_students()
display_students_data(students)
