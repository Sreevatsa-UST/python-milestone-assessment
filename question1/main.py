# Assessment Objective
# This milestone assessment is designed to evaluate the participant's understanding of basic Python programming concepts through simple, practical, scenario-based tasks.
# Question 1 — Student Marks Management System
# Scenario
# You are asked to develop a simple Python program to manage student marks. The program should accept details of multiple students, calculate their results, and display a summary.
# Requirements
# 1.	Store the following information for each student: Student ID, Student Name, Python Marks, SQL Marks, and AI Marks.
# 2.	Calculate Total Marks, Average Marks, and Grade.
# 3.	Display whether the student is PASS (average >= 40) or FAIL (average < 40).
# 4.	Display the student who has the highest average.
# 5.	Display the list of students who scored more than 75 average marks.
# 6.	Use appropriate Lists, Dictionaries, Functions, Conditional Statements, and Loops.
# 7.	Use at least one List Comprehension.
# 8.	Display the final result in a readable format.
# Sample Output
# ===== Student Result =====

# Student ID: 101
# Name: Rahul
# Total: 240
# Average: 80
# Grade: A
# Result: PASS

# Student ID: 102
# Name: Anjali
# Total: 195
# Average: 65
# Grade: B
# Result: PASS

# Student Marks Managenet Application

# Calculate Average Marks 

def get_average(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

students = []

# Number of students
n = int(input("Enter Number of Students: ")) 

for i in range(n):
    print("\nEnter Student Detials")
    
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    python_marks = int(input("Enter Python Marks: "))
    sql_marks = int(input("Enter SQL Marks: "))
    ai_marks = int(input("Enter AI Marks: "))

    total_marks = python_marks + sql_marks + ai_marks
    average_marks = total_marks / 3

    grade = get_average(average_marks)

    if average_marks >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    student_data = {
        "id": student_id,
        "name": student_name,
        "total": total_marks,
        "average": average_marks,
        "grade": grade,
        "result": result
    }

    students.append(student_data)

print("\n***** Student Results *****")

for s in students:
    print("\nStudent ID:", s["id"])
    print("Student Name: ", s["name"])
    print("Student Total: ", s["total"])
    print("Average: ", s["average"])
    print("Grade :", s["grade"])
    print("Result: ", s["result"])
    print("******************************")

# Heighest Average Makes Scored by a Student
highest_student_marks = students[0]

for s in students:
    if s["average"] >= highest_student_marks["average"]:
        highest_student_marks = s

# Student marks above 75 
marks_above_75 = [s["name"] for s in students if s["average"] > 75]

print("\n***** Students above 75 Marks *****")
print("Students with Highest Score:", highest_student_marks["name"])

if len(marks_above_75) > 0:
    print("Students above 75:", ", ".join(marks_above_75))
else:
    print("No student scored above 75")

