# Question 2 — Simple Employee File Management
# Scenario
# You are working on a small Python application that maintains employee information. Employee details need to be stored in a file and later read to generate a simple report.
# Requirements
# 9.	Create a file called employees.txt.
# 10.	Store employee details such as: Employee ID, Name, Role, and Salary.
# 11.	Read the employee information from the file.
# 12.	Display all employees.
# 13.	Find and display employees whose salary is greater than ₹50,000.
# 14.	Find the employee with the highest salary.
# 15.	Count how many employees belong to each role.
# 16.	Use functions such as add_employee(), read_employees(), find_highest_salary(), and find_employees_by_role().
# 17.	Use a context manager (with open()) while working with the file.
# 18.	Handle the situation where the file does not exist using exception handling.
# 19.	Create a simple Employee class with employee_id, name, role, and salary.
# 20.	Create a method such as display_details().
# Sample Employee Data
# 101,Rahul,Python Developer,50000
# 102,Anjali,Tester,45000
# 103,John,Developer,60000
# 104,Priya,Tester,48000
# Sample Output
# ===== Employee Details =====

# 101 - Rahul - Python Developer - ₹50000
# 102 - Anjali - Tester - ₹45000
# 103 - John - Developer - ₹60000
# 104 - Priya - Tester - ₹48000

# ===== Employees with Salary > 50000 =====

# John - ₹60000

# Highest Paid Employee:
# John - ₹60000

# Employee File Managenent
class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - {self.salary}")

# Write Employee Details
def add_employee():
    with open("employees.txt", "w") as file:
        file.write("Emp001,Sam,Quality Assurance,60000\n")
        file.write("Emp002,Jenny,Full Stack Developer,80000\n")
        file.write("Emp003,Tim,IT Support,55000\n")
        file.write("Emp004,Jan,Operations,40000\n")

# Read employee data
def read_employees():
    employees = []

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, name, role, salary = line.strip().split(",")
                employees.append(
                    Employee(emp_id, name, role, int(salary))
                )

    except FileNotFoundError:
        print("employees.txt file not found!")

    return employees

# Employee Highest Salary
def highest_salary(employees):
    highest = employees[0]

    for emp in employees:
        if emp.salary > highest.salary:
            highest = emp

    return highest

# Employee count by roll
def employee_by_roll(employees):
    employee_role = {}

    for emp in employees:
        if emp.role in employee_role:
            employee_role[emp.role] += 1
        else:
            employee_role[emp.role] = 1
    
    return employee_role

# Adding an employee to the employee.txt file
add_employee()

# Calling read employee function
employees = read_employees()

print("***** Employee Details *****")
for emp in employees:
    emp.display_details()

print("\n***** Employees with more then 50000 Salary *****")
for emp in employees:
    if emp.salary > 50000:
        print(f"{emp.name} Salary is - ₹{emp.salary}")

highest = highest_salary(employees)

print("\nHighest Paid Employee is:")
print(f"{highest.name} - ₹{highest.salary}")

print("\nEmployee Count by Role:")
roles = employee_by_roll(employees)

for role, count in roles.items():
    print(f"{role}: {count}")