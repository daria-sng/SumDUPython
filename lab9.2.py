import json
import sys

students = {
    'Daniel Miller': [10, 11, 8, 9, 10],
    'Emma Smith': [11, 11, 12, 10, 9],
    'John Jones': [1, 5, 8, 10, 2],
    'Amelia Davis': [7, 8, 4, 6, 8],
    'James Brown': [10, 1, 7, 8, 9],
    'Charlotte Lopez': [3, 10, 12, 11, 10],
    'Thomas Wilson': [6, 4, 2, 1, 1],
    'Ava Garcia': [10, 10, 12, 10, 11],
    'Ethan Anderson': [9, 8, 10, 9, 2],
    'Ella Harris': [1, 6, 9, 10, 4]
}

json_database = json.dumps(students, indent = 4)
try: 
    with open("Database.json", "w+") as file:
        file.write(json_database)
except:
    print("Error with file \"Database.json\"!")
    sys.exit()

def printjson():
    print("\nJSON file (\"Database.json\"):")
    try:
        with open("Database.json", "r") as file:
            python_data = json.load(file)
            for name, marks in python_data.items():
                print(json.dumps({name: marks}))
    except FileNotFoundError:
        print("File Database.json not found!")
        sys.exit()
    except json.JSONDecodeError:
        print("Error with json format!")

def add(python_data, key, marks):
    python_data[key] = marks
    try:
        with open("Database.json", "w") as file:
            json.dump(python_data, file, indent = 4)
    except:
        print("File \"Database.json\" not found!")
        sys.exit()
    print(f"Student {key} was successfully added!")

def delete(python_data, key):
    del python_data[key]
    try: 
        with open("Database.json", "w") as file:
            json.dump(python_data, file, indent = 4)
    except:
        print("File \"Database.json\" not found!")
        sys.exit()
    print(f"Student {key} was successfully deleted!")

def search(name, python_data):
    if name in python_data:
        print(f"{name}: {python_data[name]}")
    else:
        print("This student is not found in file \"Marks.json\"!")

def review(python_data):
    sumData = {}
    for function in [max, min]:
        student = function(python_data, key=lambda name: sum(python_data[name]))
        sumData[student] = python_data[student]
        sumData[f"Sum of {student}"] = sum(python_data[student])
    
    try:
        with open("Marks.json", "w+") as file:
            json.dump(sumData, file, indent=4)
    except:
        print("Error with file \"Marks.json\"!")
        sys.exit()
    print(f"File \"Marks.json\" created successfully and added result!")

while True:
    try:
        print("\nJSON file \"Database.json\"")
        option = int(input("\nEnter option number:\n1 - Output the contents of a JSON file\n2 - Add a new information to the JSON file\n3 - Delete the information from the JSON file\n4 - Search for data in a JSON file by name\n5 - Name and surname of students with the highest and lowest marks\n6 - Exit\n"))
        if option == 1:
            printjson()
        if option == 2:
            key = input("Enter new student: ")
            try:
                with open("Database.json", "r") as file:
                    python_data = json.load(file)
            except:
                print("File \"Database.json\" not found!")
                sys.exit()

            if key in python_data:
                print("This student is in the JSON file (\"Database.json\"), try another student!")
            else:
                marks = list(map(int, input("Enter new 5 grades: ").split()))
                while len(marks) != 5:
                    marks = list(map(int, input("Please enter exactly 5 grades: ").split()))
                add(python_data, key, marks)
        if option == 3:
            key = input("Enter student for delete: ")
            try:
                with open("Database.json", "r") as file:
                    python_data = json.load(file)
            except:
                print("File \"Database.json\" not found!")
                sys.exit()

                if key in python_data:
                    delete(python_data, key)
                else:
                    print("This student is not in the JSON file (\"Database.json\"), try another student!")
        if option == 4:
            name = input("Enter student to search: ")
            try:
                with open ("Database.json", "r") as file:
                    python_data = json.load(file)
            except:
                print("File \"Database.json\" not found!")
                sys.exit()
            search(name, python_data)
        if option == 5:
            try:
                with open ("Database.json", "r") as file:
                    python_data = json.load(file)
            except:
                print("File \"Database.json\" not found!")
                sys.exit()
            review(python_data)
        if option == 6:
            print("Exit")
            break
    except ValueError:
        print("Please, enter only numbers!")
    except FileNotFoundError:
        print("File Database.json not found!")