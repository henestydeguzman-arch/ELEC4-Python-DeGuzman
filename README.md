# ELEC 4 - Python Programming

## Student Information

- Name: Henesty G. De Guzman
- Section: IV-BSIT A
- Course: ELEC 4 - Python Programming

## About

This repository contains my Set 1 activities for the self-paced learning assignment in Python Programming. Through these activities, I practiced using functions, modules, lists, sets, and exception handling.

## Set 1 Activities

| Activity | Description |
| --- | --- |
| [P1 - Student Grade Calculator](set1/p1/) | Calculates student grades using functions. |
| [P2 - Custom Module](set1/p2/) | Uses a separate module for grade calculations. |
| [P3 - Student Record Manager](set1/p3/) | Manages student names using lists and sets. |
| [P4 - Safe Menu Program](set1/p4/) | Handles errors using exception handling. |

## How to Run

Make sure Python 3 is installed. Open CMD or the terminal inside the repository folder. Run each activity using the commands below.

## P1 - Student Grade Calculator

I created a menu-driven program that calculates the average, highest grade, lowest grade, and pass or fail status of a student using functions.

```cmd
python set1/p1/p1_grade_calculator.py
```

### Program Output

Passed Result

![Passed Result](set1/p1/screenshots/P1_Output_Passed.png)

Failed Result

![Failed Result](set1/p1/screenshots/P1_Output_Failed.png)

## P2 - Custom Module

I separated the grade calculation functions into a module called student_utils.py and imported them into my main program so I could reuse the functions.

```cmd
python set1/p2/p2_main.py
```

### Program Output

Passed Result

![Passed Result](set1/p2/screenshots/P2_Output_Passed.png)

Failed Result

![Failed Result](set1/p2/screenshots/P2_Output_Failed.png)

## P3 - Student Record Manager

I created a program that allows users to add, remove, search, and display student names. I used a list and a set to manage the names and prevent duplicate entries.

```cmd
python set1/p3/p3_record_manager.py
```

### Program Output

Add Student

![Add Student](set1/p3/screenshots/Add_Student.png)

Display Students

![Display Students](set1/p3/screenshots/Display_Students.png)

Duplicate Prevention

![Duplicate Prevention](set1/p3/screenshots/Duplicate_Prevention.png)

Remove Student

![Remove Student](set1/p3/screenshots/Remove_Students.png)

Search Student

![Search Student](set1/p3/screenshots/Search_Students.png)

## P4 - Safe Menu Program

I used exception handling to handle invalid input, division by zero, and missing files without crashing the program.

```cmd
cd set1\p4
python p4_exceptions.py
```

Use test.txt to test the file opening option. After exiting the program, return to the repository folder using:

```cmd
cd ..\..
```

### Program Output

Division by Zero

![Division by Zero](set1/p4/screenshots/Division%20By%20Zero.png)

Invalid Menu Choice

![Invalid Menu Choice](set1/p4/screenshots/Invalid%20Menu%20Choice.png)

Invalid Number

![Invalid Number](set1/p4/screenshots/Invalid%20Number.png)

Missing File

![Missing File](set1/p4/screenshots/Missing%20File.png)

## Reference

- [Bro Code - Python Full Course](https://www.youtube.com/watch?v=ix9cRaBkVe0)
