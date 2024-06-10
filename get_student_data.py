employees = []


flag = True
summ = 0
for i in range(1000000000000):
    is_continue = input("for continue press 'y' or press any key to exit ")
    if is_continue == 'y' or is_continue == "Y":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        summ += salary

        employee =  [name, age, salary]
        employees.append(employee)
    else:
        break

print('Total salary is: ', summ)
# print(employees)
print('Name',"\t",'Age',"\t",'Salary')
for emp in employees:
    print(emp[0],"\t", emp[1],"\t", emp[2])
    # print('Name :', emp[0])
    # print('Age :', emp[1])
    # print('Salary :', emp[2])
    
