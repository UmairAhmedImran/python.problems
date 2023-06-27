number_of_employees = int(input("Enter number of employees: "))
employee_list = []
for i in range(1, number_of_employees + 1):
    print("\n---------------------------")
    employee_id = input("Enter employee id: ")
    last_name = input("Enter employee last name: ")
    first_name = input("Enter employee first name: ")
    salary = int(input("Enter employee salary: "))
    print("---------------------------\n")
    if not (salary > 0 and salary <= 10000):
        print("Invalid salary")
        break
    employee_list.append(employee_id)
    employee_list.append(last_name.capitalize())
    employee_list.append(first_name.capitalize())
    employee_list.append(salary)

print(f"list of employees {employee_list}")
    
