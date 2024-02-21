import os
import globals
def save():
    # if we did load the data and data was changed
    if globals.loaded and (globals.added or globals.updated or globals.deleted):
        # overwrite file
        with open("database.txt", "w") as f:
            for key, value in globals.students.items():
                f.write(str(key) + "/\n")
                f.write(
                    f"first_name:{value['first_name']};last_name:{value['last_name']};email:{value['email']};gender:{value['gender']};age:{value['age']};address:{value['address']};gpa:{value['gpa']}/\n"
                )

    else:
        # append if only new data worked on
        with open("database.txt", "a") as f:
            for key, value in globals.students.items():
                f.write(str(key) + "/\n")
                f.write(
                    f"first_name:{value['first_name']};last_name:{value['last_name']};email:{value['email']};gender:{value['gender']};age:{value['age']};address:{value['address']};gpa:{value['gpa']}/\n"
                )
    print("------- Your changes are saved! -------")


def load():
    globals.loaded = True
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

                globals.students[int(st[i])] = data_dict

        if globals.added:
            # sort the dictionary after loading to avoid future bugs
            keys = list(globals.students.keys())
            keys.sort()
            globals.students = {key: globals.students[key] for key in keys}
        print("---------- Data sucessfully loaded! ----------")

    else:
        print("--------------- No data to load ---------------")


# this should be called before starting the program to normalize the data
def get_last_id():
    if os.path.exists("database.txt"):
        with open("database.txt") as f:
            st = f.read().strip()
            if st:
                st = st.split("/")
                globals.id = int(st[-3])
