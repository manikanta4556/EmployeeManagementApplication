# Employee Management Application Using Python - Manikanta Developer

from os import system
from datetime import datetime
import re

# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(host="localhost", user="root", password="",database="employee")


# Function to validate_date_of_birth
def validate_date_of_birth(Date_of_birth):
    try:
        # convert the input string to a datetime object
        date_object = datetime.strptime(Date_of_birth, '%Y-%m-%d')
        
        # Check if the year is within a reasonable range (e.g., not in the future)
        current_year = datetime.now().year
        if date_object.year > current_year or date_object.year < (current_year - 150):
            return False

        
        return True
    except ValueError:
        
        return False


# Function to Add_Employ
def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking If Employee Name is Exit Or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Age = input("Enter Employee Age: ")
    Date_of_birth = input("Enter Employee Date Of Birth: ")
    if(validate_date_of_birth(Date_of_birth)):
        print("Valid Date Of Birth")
    else:
        print("Invalid Date Of Birth")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Salary = input("Enter Employee Salary: ")
    Department = input("Enter Employee Department: ")
    data = (Id, Name, Age, Date_of_birth, Salary, Department)
    # Instering Employee Details in
    # the Employee (empdata) Table
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()

# Function To Check if Employee With given Name Exist or not
def check_employee_name(employee_name):
    # query to select all Rows from employee(empdata) table
    sql = 'select * from empdata where Name=%s'

    # making cursor buffered to make rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number of row a with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function To Check if Employee With
# given Id Exist or not
def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'select * from empdata where Id=%s'

    # making cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of row a with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False

# Function to Display_Employ
def Filter_Employ():
    print("{:>60}".format("-->> Filter Employee Record <<--"))
    system("cls")
    print("1. Filter By Department")
    print("2. Filter By Name")
    print("3. Filter By Age")
    print("4.Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Department=input('Enter Department: ')
        sql = 'select * from empdata where Department=%s'
        data = (Department,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)
        #fetching details of the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Age: ", i[2])
            print("Employee Date of Birth: ", i[3])
            print("Employee Salary: ", i[4])           
            print("Employee Department: ", i[5])
            
            print("\n")
        press = input("Press Any key To Continue..")
        menu() 

        
    elif ch == 2:
        system("cls")
        Name=input('Enter Name : ')
        sql = 'select * from empdata where Name = %s'
        data = (Name,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)
        #fetching details of the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Age: ", i[2])
            print("Employee Date of Birth: ", i[3])
            print("Employee Salary: ", i[4])           
            print("Employee Department: ", i[5])
            
            print("\n")
        press = input("Press Any key To Continue..")
        menu() 
    elif ch == 3:
        system("cls")
        Age=input('Enter Age : ')
        sql = 'select * from empdata where Age = %s'
        data = (Age,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)
        #fetching details of the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Age: ", i[2])
            print("Employee Date of Birth: ", i[3])
            print("Employee Salary: ", i[4])           
            print("Employee Department: ", i[5])
            
            print("\n")
        press = input("Press Any key To Continue..")
        menu() 
    elif ch == 4:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()

# Function to Update_Employ
def Update_Employ():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Date_of_birth= input("Enter Employee Date Of Birth: ")
        if(validate_date_of_birth(Date_of_birth)):
            print("Valid Date Of Birth")
        else:
            print("Invalid Date Of Birth")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Age = input("Enter Employee Age: ")
        Salary = input("Enter Employee Salary: ")
        Department = input("Enter Employee Department: ")
        # Updating Employee details in empdata Table
        sql = 'UPDATE empdata set Date_of_birth = %s, Age = %s, Salary = %s, Department = %s where Id = %s'
        data = (Date_of_birth, Age, Salary, Department, Id)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()

# Function to Delete_Employ
def Delete_Employ():
    print("{:>60}".format("-->> Delete Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to delete Employee from empdata table
        sql = 'delete from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)

        #commit() method to make changes in the empdata table
        con.commit()
        print("Employee Deleted")
        press = input("Press Any key To Continue..")
        menu()

# Function to Show_All_Employes
def Show_All_Employes():
    print("{:>60}".format("-->> Show All Employes Records <<--\n"))
    #query to show all employees from empdata table
    sql = 'select * from empdata'
    c = con.cursor()
        
    #executing the sql query
    c.execute(sql)

    #fetching all details of all the employee
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Age: ", i[2])
        print("Employee Date of Birth: ", i[3])
        print("Employee Salary: ", i[4])           
        print("Employee Department: ", i[5])
            
        print("\n")
    press = input("Press Any key To Continue..")
    menu() 

# Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking If Employee Id is Exit Or Not
    if(check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        #query to search Employee from empdata table
        sql = 'select * from empdata where Id = %s'
        data = (Id,)
        c = con.cursor()
        
        #executing the sql query
        c.execute(sql, data)

        #fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Age: ", i[2])
            print("Employee Date of Birth: ", i[3])
            print("Employee Salary: ", i[4])
            print("Employee Department: ", i[5])
            
            print("\n")
        press = input("Press Any key To Continue..")
        menu()

#Function to get Agerage Salary of an Employee
def Average_Salary_Of_An_Employee():
    # Query the database for salaries
    query = "SELECT salary FROM empdata"
    c = con.cursor()
    c.execute(query)

    salaries = [row[0] for row in c.fetchall()]

    # Calculate the average salary
    if salaries:
        average_salary = sum(salaries) / len(salaries)
        print(f"The average salary in the company is ${average_salary:.2f}")
    else:
        print("No salary data available.")
    press = input("Press Any Key To Continue..")
    menu()

#Function to get Average Salary of a Department
def Average_Salary_Of_Department():
    Department=input('Enter Department: ')
    # Query the database for salaries
    sql = "select salary from empdata where Department = %s"
    data = (Department,)
    c = con.cursor()
    c.execute(sql,data)
    salaries = [row[0] for row in c.fetchall()]

    # Calculate the average salary
    if salaries:
        average_salary = sum(salaries) / len(salaries)
        print(f"The average salary of a Department is ${average_salary:.2f}")
    else:
        print("No salary data available.")
    press = input("Press Any Key To Continue..")
    menu()
        

# Menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management Application <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Show all Employees")
    print("3. Filter Employees based on criteria")
    print("4. Search Employee Record")
    print("5. Update Employee Record")
    print("6. Delete Employee Record")
    print("7.Average Salary Of An Employee")
    print("8.Average Salary Of a Department")
    print("9. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7/8] <<--"))

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Show_All_Employes()
    elif ch == 3:
        system("cls")
        Filter_Employ()
    elif ch == 4:
        system("cls")
        Search_Employ()
    elif ch == 5:
        system("cls")
        Update_Employ()
    elif ch == 6:
        system("cls")
        Delete_Employ()
    elif ch == 7:
        system("cls")
        Average_Salary_Of_An_Employee()
    elif ch == 8:
        system("cls")
        Average_Salary_Of_Department()
    elif ch == 9:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue..")
        menu()


# Calling menu function
menu()
