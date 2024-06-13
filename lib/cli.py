from model_1 import Department, Employee

class CLI:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Manage Departments")
            print("2. Manage Employees")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.department_menu()
            elif choice == '2':
                self.employee_menu()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def department_menu(self):
        while True:
            print("\nDepartment Menu:")
            print("1. Create Department")
            print("2. Delete Department")
            print("3. View All Departments")
            print("4. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_department()
            elif choice == '2':
                self.delete_department()
            elif choice == '3':
                self.view_all_departments()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def employee_menu(self):
        while True:
            print("\nEmployee Menu:")
            print("1. Create Employee")
            print("2. Delete Employee")
            print("3. View All Employees")
            print("4. View Employees by Department ID")
            print("5. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_employee()
            elif choice == '2':
                self.delete_employee()
            elif choice == '3':
                self.view_all_employees()
            elif choice == '4':
                self.view_employees_by_department()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def view_employees_by_department(self):
        department_id = int(input("Enter department ID to view employees: "))
        employees = Employee.get_by_department_id(department_id)
        if employees:
            print("\nEmployees in Department {}:".format(department_id))
            for employee in employees:
                print(employee)
        else:
            print("No employees found in Department {}.".format(department_id))

    def create_department(self):
        name = input("Enter department name: ")
        Department.create(name)
        print("Department created successfully.")

    def delete_department(self):
        department_id = int(input("Enter department ID to delete: "))
        Department.delete(department_id)
        print("Department deleted successfully.")

    def view_all_departments(self):
        departments = Department.get_all()
        if departments:
            print("\nAll Departments:")
            for department in departments:
                print(department)
        else:
            print("No departments found.")

    def create_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        department_id = int(input("Enter employee department ID: "))
        Employee.create(name, age, salary, department_id)
        print("Employee created successfully.")

    def delete_employee(self):
        employee_id = int(input("Enter employee ID to delete: "))
        Employee.delete(employee_id)
        print("Employee deleted successfully.")

    def view_all_employees(self):
        employees = Employee.get_all()
        if employees:
            print("\nAll Employees:")
            for employee in employees:
                print(employee)
        else:
            print("No employees found.")

if __name__ == "__main__":
    cli = CLI()
