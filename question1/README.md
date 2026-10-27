>Problem Statement

A simple Python application developed to manage student marks and generate a result summary. The program collects student information, calculates total marks, average marks, grade, and pass/fail status. It also identifies the highest-scoring student and displays students whose average marks are above 75.

>Approach / Logic Used
Student information is stored using a list of dictionaries.
A function is used to calculate grades based on average marks.
Total and average marks are calculated for each student.
Conditional statements determine whether a student has passed or failed.
Loops are used to process and display student records.
A list comprehension is used to find students scoring above 75 average marks.
The highest-scoring student is identified by comparing average scores.

>Python Concepts Used
Lists
Dictionaries
Functions
Loops
Conditional Statements
List Comprehension
Calculations and Data Processing
Output Formatting

<!-- Student Marks Output  -->

$ python student_marks.py
Enter Number of Students: 3

Enter Student Detials
Enter Student ID: 101
Enter Student Name: Ed
Enter Python Marks: 96
Enter SQL Marks: 86
Enter AI Marks: 68

Enter Student Detials
Enter Student ID: 102
Enter Student Name: Edd
Enter Python Marks: 86
Enter SQL Marks: 67
Enter AI Marks: 86

Enter Student Detials
Enter Student ID: 103
Enter Student Name: Eddy
Enter Python Marks: 34
Enter SQL Marks: 53
Enter AI Marks: 22

***** Student Results *****

Student ID: 101
Student Name:  Ed
Student Total:  250
Average:  83.33333333333333
Grade : A
Result:  PASS
******************************

Student ID: 102
Student Name:  Edd
Student Total:  239
Average:  79.66666666666667
Grade : A
Result:  PASS
******************************

Student ID: 103
Student Name:  Eddy
Student Total:  109
Average:  36.333333333333336
Grade : F
Result:  FAIL
******************************

***** Students above 75 Marks *****
Students with Highest Score: Ed
Students above 75: Ed, Edd
