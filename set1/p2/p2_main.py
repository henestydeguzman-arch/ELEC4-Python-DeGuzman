# I imported my student_utils module so I can use the functions I created.
import student_utils

# I imported the functions directly so I can call them by their names.
from student_utils import cal_avg, grades_status, high_grade, low_grade

# I imported math so I can use ceil to round up the average.
import math

print('====STUDENT GRADE CALCULATOR====')

# I created an empty list to store the grades.
grades = []

num_grades = int(input("Enter Number of Grades: "))

# I used a loop to ask for grades based on the number of subjects.
for number in range(num_grades):
    while True:
        grade = float(input(f"Enter Your Grade for Subject {number + 1}: "))

        
        if grade >= 0 and grade <= 100:
            grades.append(grade)  
            break  # break function will stop the loop if the grade is valid.
        else:
            print("Please Enter Grade between 0 and 100.")

print("\nGrade Successfully Computed!!")

print('====STUDENT GRADE RESULT====')

average = cal_avg(grades)
print("Average:", math.ceil(average))   # I used math.ceil to round the average to the next whole number.

print("Highest Grade:", student_utils.high_grade(grades))
print("Lowest Grade:", student_utils.low_grade(grades))
print("Grade Result:", grades_status(grades))
print("===============================")