import json

loaded_students = {}
students = {
    'id 1': {'name': 'John', 'age': 30 ,'grade' : 'A'},
    'id 2': {'name': 'Alice', 'age': 25,'grade' : 'B'},
    'id 3': {'name': 'Bob', 'age': 35,'grade' : 'C'}
}

num = input()
key = 'id ' + num

# to write into the json file
with open('students.json', 'w') as f:
    json.dump(students, f)

# to read into the json file
with open('students.json', 'r') as f:
    loaded_students = json.load(f)
                        #.values()  -> to access a value
                        #.value -> get key value
loaded_students[key] = {'name': 'amr', 'age': '21' , 'grade': 'A'}

# # try & catch
# if key in loaded_students.keys():
#     print('this user already exists, do you want to update')

print("Loaded Dictionary:", loaded_students)

