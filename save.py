import pandas as pd


class Database:
    students = {}

    def __init__(self) -> None:
        pass

    def add(self):
        # this is supposed to add multiple students
        while True:
            id = input("Enter student's id: ")
            # confirmation
            while not id.isdigit():
                # raise an error or reprompt
                pass
            name = input("Enter student's name: ")
            while not name.isalpha():
                pass
            grade = input("Enter student's gpa: ")
            while not grade.isdigit():
                pass
            age = input("Enter student's age: ")
            while not age.isdigit():
                pass
            result = self.students.get(id)

            if result == None:  # if no user with the id given, add the user
                self.students[id] = {"name": name}

            else:  # raise an arror or reprompt
                pass
            ask = input("do you want to add other users y/n? ")
            if ask.lower() == "n":
                break

    def save(self):
        student_ids = list(self.students.keys())
        names = []
        for data in self.students.values():
            names.append(data['name'])
        df = pd.DataFrame({"id": student_ids,'name':names})

        try:  # if file is empty this will throw an exception
            file = pd.read_csv("sample.csv")
            df.to_csv("sample.csv", mode="a", index=False, header=False)

        except Exception:  # if empty
            df.to_csv("sample.csv", index=False)


x = Database()
x.add()
x.save()
