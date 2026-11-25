# Henesty G. De Guzman
# IV BSIT - A
# P3: Student Record Manager
# Date: November 18, 2026

students = []  # use to store and display student names
student_set = set() # it is use to check kung may duplicate name


def add_student():

    while True:
        student = input(f'Enter Student (Exit to Quit): ')
        if student.lower() == 'exit':
            break
        elif student == '':
            print('Error: Please Input Name!')
        elif student.lower() in student_set:
            print('Name is Already Exist')
        else:
            students.append(student)
            student_set.add(student.lower())
            students.sort(key=str.lower)
            print('Student Name Successfully Added!')

def remove_student():
    while True:
        student_remove = input('Enter Student Name to Remove (Exit to Quit): ')
        if student_remove.lower() == 'exit':
            break
        elif student_remove.lower() in student_set:

            for name in students:
                if name.lower() == student_remove.lower():
                    students.remove(name)
                    student_set.discard(name.lower())
                    break
            print('Student Successfully Removed!')
        else:
            print('Student Name Not Found!')

def search_student():
   
        student_search = input('Enter Student Name(Exit to Quit): ')
        if student_search.lower() == 'exit':
            return

        found = False
        for name in students:
            if student_search.lower() in name.lower():
                print(f'Student Found: {name}')
                found = True
        if found == False:
            print(f'Student Name {student_search} is Not Found!')


def display_students():

    print('======STUDENT NAMES======')
    for number, student in enumerate(sorted(students, key=str.lower), start=1):
        print(f'{number}. {student}')
        
    print('=========================')
    print(f'Total Students: {len(students)}')

while True: 
    print("\n=====STUDENT RECORD MANAGER=====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search")
    print("4. Display Students")
    print("5. Exit")

    menu = input("Enter Menu Number: ")

    if menu == "1":
        add_student()
    elif menu == "2":
        remove_student()
    elif menu == "3":
        search_student()
    elif menu == "4":
        display_students()
    elif menu == "5":
        print("Exit Student Record Manager")
        break
    else:
        print("Invalid! Please Try Again!")


# Difference between list and set
# A list is ordered, changeable and you can duplicate values, so i used this to store and display student names in ordered.
# while the set is unordered, immutable and you cannot duplicate values, so i used this to check and to not allow duplicate values.
# So the difference of the two is that they have different rules in duplicate values.