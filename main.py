# add employees to your company with python
from entity.Employee import Employee

available_workers = []

# this func check the employees experience
def checkEmployee(employee, required_experience):
    if (employee.get_excperience() > required_experience):
        available_workers.append(employee)
        return f"{employee.get_name()} is added to the 'available_workers' list."
    else:
        return f"{employee.get_name()} is not available to join 'available_workers' list."

# here we operate the cycle to add employee and sort by required experience 
is_going = True
required_experience = 0
while is_going:

    want_to_add = input("Do you want to add an employee to your company? (y/n): ")

    if want_to_add in ["y","yes"]:
        try:
            employee_name = input("Enter employee name: ")
            print("ok")
            employee_experience = int(input("Enter employee experience? (in year) : "))
            print("got it.")

            employee = Employee(employee_name,employee_experience)

            # sort employee by experience
            
            if required_experience <= 0 :
                print("Now we have employees in list. We can sort employees by experience!")
                required_experience = int(input("Enter required experience ? (in year) :"))
            else:
                pass
            
            result = checkEmployee(employee, required_experience)
            print(result)
            
        except ValueError:
            print("Invalid input! Please enter number for required experience.")

    else :
        is_going = False

print("-------> (left code True) <-------")
print("All available employees in the 'available_workers' list: ")
counts = 1
if available_workers:
    for employee in available_workers:
        print(f"{counts}){employee.get_name()} with the experience of working {employee.get_excperience()} years")
        counts += 1
else: 
    print("No employees met the required experience criteria.")


