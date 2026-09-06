#Combined Python Concepts — Student Management Program
#=====================================================

import math


# ==============================
# Parent Class
# ==============================
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# ==============================
# Child Class
# ==============================
class Student(Person):

    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 40:
            return "C"
        else:
            return "Fail"

    def display_student(self):
        self.display_person()
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())


# ==============================
# Function
# ==============================
def add_student():

    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        marks = []

        print("\nEnter marks for 3 subjects:")

        for i in range(1, 4):
            mark = float(input(f"Enter mark {i}: "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        student = Student(name, age, course, marks)

        return student

    except ValueError:
        print("Invalid input. Please enter numbers where required.")
        return None


# ==============================
# Main Program
# ==============================

print("===================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("===================================")

students = []

# Add students
number = int(input("How many students do you want to add? "))

for i in range(number):

    print(f"\n--- Student {i + 1} ---")

    student = add_student()

    if student:
        students.append(student)


# ==============================
# Display Students
# ==============================

print("\n===================================")
print("         STUDENT DETAILS")
print("===================================")

for student in students:
    print("\n-----------------------------")
    student.display_student()


# ==============================
# Dictionary
# ==============================

student_data = {}

for student in students:
    student_data[student.name] = {
        "age": student.age,
        "course": student.course,
        "average": student.calculate_average(),
        "grade": student.get_grade()
    }

print("\n===================================")
print("       STUDENT DICTIONARY")
print("===================================")

print(student_data)


# ==============================
# Set
# ==============================

courses = {student.course for student in students}

print("\nUnique Courses:")
print(courses)


# ==============================
# Tuple
# ==============================

student_count = len(students)
summary = (student_count, len(courses))

print("\nSummary Tuple:")
print("Total Students:", summary[0])
print("Total Courses:", summary[1])


# ==============================
# List Comprehension
# ==============================

averages = [student.calculate_average() for student in students]

print("\nStudent Averages:")
print(averages)


# ==============================
# Lambda Function
# ==============================

if students:

    highest_student = max(
        students,
        key=lambda student: student.calculate_average()
    )

    print("\nHighest Scoring Student:")
    print(highest_student.name)
    print(highest_student.calculate_average())


# ==============================
# Math Module
# ==============================

if students:

    highest_average = max(averages)

    print("\nMath Module Example:")
    print("Square Root of Highest Average:",
          math.sqrt(highest_average))


# ==============================
# File Handling
# ==============================

try:

    with open("students.txt", "w") as file:

        file.write("STUDENT REPORT\n")
        file.write("====================\n")

        for student in students:

            file.write(
                f"Name: {student.name}\n"
                f"Age: {student.age}\n"
                f"Course: {student.course}\n"
                f"Marks: {student.marks}\n"
                f"Average: {student.calculate_average():.2f}\n"
                f"Grade: {student.get_grade()}\n"
                f"--------------------\n"
            )

    print("\nStudent data saved to students.txt")


    # Read file
    with open("students.txt", "r") as file:

        content = file.read()

    print("\n===================================")
    print("        FILE CONTENT")
    print("===================================")

    print(content)


except IOError:
    print("Error while accessing the file.")


# ==============================
# Final Result
# ==============================

print("\n===================================")
print("          PROGRAM COMPLETED")
print("===================================")

"""
Concepts used in this one program
Variables → name, age, course, marks
Data types → str, int, float, bool
Input/Output → input(), print()
Operators → +, /, <, >, ==
Conditions → if, elif, else
Loops → for
List → marks, students, averages
Tuple → summary
Dictionary → student_data
Set → courses
Functions → add_student(), calculate_average()
Exception handling → try, except
Classes & Objects → Person, Student
Inheritance → Student(Person)
super() → calling the parent constructor
List comprehension → [student.calculate_average() ...]
Lambda function → finding the highest-scoring student
Module → math
File handling → open(), reading and writing files
with statement → safely handling files

This is essentially a small Student Management System, so you can use it as a single practice project 
to understand how the individual Python concepts work together.

"""

'''
OUTPUT:
=======

PS C:\Users\varshini\Python Code> & C:\Users\varshini\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/varshini/Python Code/Concepts.py"
===================================
       STUDENT MANAGEMENT SYSTEM
===================================
How many students do you want to add? 2

--- Student 1 ---
Enter student name: Raja
Enter age: 26
Enter course: BCA

Enter marks for 3 subjects:
Enter mark 1: 89
Enter mark 2: 87
Enter mark 3: 99

--- Student 2 ---
Enter student name: Vishnu
Enter age: 26
Enter course: BTech

Enter marks for 3 subjects:
Enter mark 1: 98
Enter mark 2: 99
Enter mark 3: 100

===================================
         STUDENT DETAILS
===================================

-----------------------------
Name: Raja
Age: 26
Course: BCA
Marks: [89.0, 87.0, 99.0]
Average: 91.66666666666667
Grade: A

-----------------------------
Name: Vishnu
Age: 26
Course: BTech
Marks: [98.0, 99.0, 100.0]
Average: 99.0
Grade: A

===================================
       STUDENT DICTIONARY
===================================
{'Raja': {'age': 26, 'course': 'BCA', 'average': 91.66666666666667, 'grade': 'A'}, 'Vishnu': {'age': 26, 'course': 'BTech', 'average': 99.0, 'grade': 'A'}}

Unique Courses:
{'BTech', 'BCA'}

Summary Tuple:
Total Students: 2
Total Courses: 2

Student Averages:
[91.66666666666667, 99.0]

Highest Scoring Student:
Vishnu
99.0

Math Module Example:
Square Root of Highest Average: 9.9498743710662

Student data saved to students.txt

===================================
        FILE CONTENT
===================================
STUDENT REPORT
====================
Name: Raja
Age: 26
Course: BCA
Marks: [89.0, 87.0, 99.0]
Average: 91.67
Grade: A
--------------------
Name: Vishnu
Age: 26
Course: BTech
Marks: [98.0, 99.0, 100.0]
Average: 99.00
Grade: A
--------------------


===================================
          PROGRAM COMPLETED
===================================
PS C:\Users\varshini\Python Code> 

'''