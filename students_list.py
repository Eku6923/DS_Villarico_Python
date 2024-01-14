students = {}
print("Enter three classmates' student number and first name:")
for i in range(3):
    number = input("Student " + str(i + 1) + " number: ")
    while len(number) != 11:
        print("Invalid student number. Please enter an 11-digit number.")
        number = input("Student " + str(i + 1) + " number: ")
    name = input("Student " + str(i + 1) + " first name: ")
    students[number] = name
print("The keys and values of the map are:")
for key, value in students.items():
    print(key, value)
print("Deleting the mapping of the third entry...")
del students[list(students.keys())[2]]
number = input("Enter your student number: ")
while len(number) != 11:
    print("Invalid student number. Please enter an 11-digit number.")
    number = input("Enter your student number: ")
name = input("Enter your first name: ")
students[number] = name
print("The entries in separate lines are:")
for key, value in students.items():
    print(key, value)
