>Problem Statement

This application manages employee records using text file storage. Employee details are stored in a file, read back into the program, and used to generate reports such as highest-paid employee, employees earning above ₹50,000, and employee count by role.

>Approach / Logic Used
An Employee class is created with employee ID, name, role, and salary attributes.
The constructor initializes employee details.
A display method is used to print employee information.
Employee records are written to and read from a text file (employees.txt).
File handling is performed using the with open() context manager.
Exception handling is used to manage missing file scenarios.
Functions are used to keep the code modular and readable.
Dictionaries are used to calculate employee count by role.

>Python Concepts Used
File Handling
Context Manager (with open())
Exception Handling (try-except)
Classes and Objects
Constructors (__init__)
Methods
Functions
Lists
Dictionaries
Loops and Conditional Statements
Object-Oriented Programming (OOP)

<!-- Employee Detials Output -->

$ python main.py
***** Employee Details *****
Emp001 - Sam - Quality Assurance - 60000
Emp002 - Jenny - Full Stack Developer - 80000
Emp003 - Tim - IT Support - 55000
Emp004 - Jan - Operations - 40000

***** Employees with more then 50000 Salary *****
Sam Salary is - ₹60000
Jenny Salary is - ₹80000
Tim Salary is - ₹55000

Highest Paid Employee is:
Jenny - ₹80000

Employee Count by Role:
Quality Assurance: 1
Full Stack Developer: 1
IT Support: 1
Operations: 1
