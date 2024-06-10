number_of_emp = int(input("Enter Your number : "))

employee = []
sum = 0

for i in range(number_of_emp):
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    salary = int(input("Enter salary : "))
    sum = sum +salary
    my_dict = {"Name":name,"Age":age,"Salary":salary }
    employee.append(my_dict)
print("Total salary of ",sum)
print(employee)
