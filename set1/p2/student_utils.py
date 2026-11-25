# print(help('modules'))
# Create a module named student_utils.py containing functions for: calculating the average,
#determining pass/fail, getting the highest grade, and getting the lowest grade.


#Function 1 is for calculating the average of grades
def cal_avg(grades):
    return sum(grades) / len(grades)


#Function 2 is for checking if the grade is passed or failed status
def grades_status(grades):
    average = cal_avg(grades)

    if average >= 75:
        return "Congrats You Passed!"
    else:
        return "Failed!"

#In Function 3 i used max to get the highest grade
def high_grade(grades):
    return max(grades)


#In Function 4 i used mmin to get the lowest grade

def low_grade(grades):
    return min(grades)

# This will display a message if I run this file directly.
if __name__ == '__main__':
    print('Student Utilities Module')