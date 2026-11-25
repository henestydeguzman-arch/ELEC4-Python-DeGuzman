# Henesty G. De Guzman
# IV BSIT - A
# P1: Student Grade Calculator
# Date: November 17, 2026

# First i created an empty list to store the grades entered by the user.
grades = [] 

# Function 1: Accept Student Grades
def enter_grades():
    global grades

    grades.clear()

    num_grades = int(input("Enter Number of Grades: "))

    for number in range(num_grades):
        while True:
            grade = float(input(f"Enter Your Grade for Subject {number + 1}: "))

            if grade >= 0 and grade <= 100:
                grades.append(grade)
                break
            else:
                print("Please Enter Grade between 0 and 100.")

    print("\nGrade Successfully Computed!!")

    
#Function 2: Compute the Average
def cal_avg(grades):
    return sum(grades) / len(grades)


#Function 3: Get the highest Grade

def high_grade(grades):
    return max(grades)


#Function 4: Get the lowest Grade

def low_grade(grades):
    return min(grades)

#Function 5: Determine the pass/fail Status

def grades_status(grades):
    average = cal_avg(grades)

    if average >= 75:
        return "Congrats You Passed!"
    else:
        return "Failed!"

# Display Results
def results():
    if len(grades) == 0:
        print("\nInvalid Please Enter Grades!")
        return
    
    print("\n=======STUDENT GRADE RESULT=======")
    print(f"Average: {cal_avg(grades):.2f}")
    print(f"Highest Grade: {high_grade(grades)}")
    print(f"Lowest Grade: {low_grade(grades)}")
    print(f"Grade Result: {grades_status(grades)}")
    print("===================================")

while True: 
    print("\n=====STUDENT GRADE CALCULATOR=====")
    print("I. Enter Grades")
    print("II. View Results")
    print("III. EXIT")

    menu = input("Enter Menu Number: ")

    if menu == "I":
        enter_grades()
    elif menu == "II":
        results()
    elif menu == "III":
        print("Exit Calculator...")
        break
    else:
        print("Invalid! Please Try Again!")


# Difference of Local and Global 
# In my code the Global Variable is grade because it should be accessed outside the functions.
# But the Local Variable is inside a function just like the num_grade inside the function enter_grades so it means that this variable can only be access inside the function.
# So the difference between this is that the local can access only inside the function and the global is can access outside the function.  
