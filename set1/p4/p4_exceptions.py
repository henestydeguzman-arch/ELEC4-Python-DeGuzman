# Henesty G. De Guzman
# IV BSIT - A
# P2: Safe Menu Program
# Date: November 18, 2026

def division():
    try:
        number1 = int(input('Enter First Number: '))
        number2 = int(input('Enter Second Number: '))
        divide = number1 / number2
    except ZeroDivisionError:
        print("You can't divide by ZERO!")
    except ValueError:
        print("Invalid Input. Please Enter Numbers Only!")
    else:
         print(divide)
    finally:
        print("Do Some Clean Up Here!")
    

def open_file():
    try:
        file_name = input('Enter File Name: ')

        with open(file_name, 'r') as file:
            content = file.read()
            print(f'File Name: {file_name} \nContent: {content}')

    except FileNotFoundError:
        print('File Not Found!')


while True: 
    print("\n=====Safe Menu Program=====")
    print("1. Division")
    print("2. Open File")
    print("3. Exit")

    menu = input("Enter Menu Number: ")

    if menu == "1":
        division()
    elif menu == "2":
        open_file()
    elif menu == "3":
        print("Exit Safe Menu Program")
        break
    else:
        print("Invalid Menu! Please Try Again!")

