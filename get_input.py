
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
