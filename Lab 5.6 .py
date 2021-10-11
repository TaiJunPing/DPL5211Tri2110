# Student ID : 1201201025
# Student Name : Tai Jun Ping

def get_bonus(unit_sold,salary):
    if(unit_sold>1000):
        bonus = (salary * 0.2)
    elif(unit_sold>=501 , unit_sold<=1000):
        bonus = (salary * 0.1)
    return bonus

def get_nett_salary(b,salary):
    nett_salary = b + salary
    return nett_salary

def display(id,salary,unit_sold,b,ns):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              SALARY SLIP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")   
    print("Staff ID                :",id)
    print("Staff salary            : RM {:.2f}".format(salary))
    print("Units sold              :",unit_sold)
    print("Bonus                   : RM {:.2f}".format(b))
    print("Nett Salary             : RM {:.2f}".format(ns))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
id = input("Enter staff id : ")
salary = float(input("Enter staff salary : RM "))
unit_sold = int(input("Enter unit sold : "))

b = get_bonus(unit_sold,salary)
ns = get_nett_salary(b,salary)
display(id,salary,unit_sold,b,ns)

