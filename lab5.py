def printdict(students):
    for key, values in students.items():
        print(f"{key} - ", end='')
        print(*values, sep=', ')

def add(students, key, new):
    students[key] = new
    print(f"New entry added - {key}")

def delete(students, key):
    del students[key]
    print(f"Deleted - {key}")

def sort(students):
    print("Dictionary entries by sorted keys: ")
    for key in sorted(students.keys()):
        print(f"{key} - ", end='')
        print(*students[key], sep=', ')

def analysis(students):
    assessment = {}
    for key, element in students.items():
        general = sum(element)
        assessment[key] = general

    student1 = max(assessment, key=assessment.get)
    student2 = min(assessment, key=assessment.get)
    maximum = assessment[student1]
    minimum = assessment[student2]
    return student1, student2, maximum, minimum


students = {
    'Elizabeth Nelson': [10, 11, 8, 9, 7, 10, 12, 8, 9, 11],
    'Joe Allen': [11, 2, 10, 8, 9, 11, 12, 8, 9, 10],
    'Alice Rivera': [8, 9, 7, 6, 10, 11, 9, 10, 11, 9],
    'Jacob Martin': [2, 4, 9, 2, 7, 6, 4, 2, 6, 8],
    'Sarah Bailey': [10, 11, 11, 12, 10, 11, 9, 10, 11, 12],
    'Peter Johnson': [7, 9, 10, 4, 10, 11, 9, 10, 8, 9],
    'Helen Adams': [10, 11, 12, 8, 9, 11, 12, 7, 10, 11],
    'Steven White': [9, 8, 7, 10, 11, 12, 8, 9, 11, 11],
    'Michelle Baker': [9, 6, 2, 6, 7, 9, 10, 11, 8, 9],
    'Harry Williams': [10, 2, 8, 6, 4, 10, 9, 8, 10, 11]
}

while True:
    try:
        option = int(input("\nEnter option number:\n1 - Output all dictionary values\n2 - Add a new entry to the dictionary\n3 - Delete an entry from the dictionary\n4 - View dictionary entries by sorted keys\n5 - Name and surname of the student with the highest sum of grades / lowest sum of grades\n6 - Exit\n"))
        if option == 6:
            print("Exit")
            break
        if option == 1:
            printdict(students)
        elif option == 2:
            key = input("Enter new key: ")
            if key in students:
                print("This key is in the dictionary, try another key!")
            else:
                new = list(map(int, input("Enter new 10 values: ").split()))
                while len(new) != 10:
                    new = list(map(int, input("Exactly 10 values: ").split()))
                else:
                    add(students, key, new)
        elif option == 3:
            key = input("Enter key: ")
            if key in students:
                delete(students, key)
            else:
                print("This key is not in the dictionary, try another key!")
        elif option == 4:
            sort(students)
        elif option == 5:
            student1, student2, maximum, minimum = analysis(students)
            print(f"Student with the highest sum of grades - {student1} {maximum}")
            print(f"Student with the lowest sum of grades - {student2} {minimum}")
    except ValueError:
        print("Enter only number!")