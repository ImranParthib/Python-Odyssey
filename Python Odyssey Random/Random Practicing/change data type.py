class Employee:
    
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
    
    def get_details(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.department)

#Class Manager:

class Manager(Employee):
    
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)
        self.employees = []
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

#Class Department:

class Department:
    
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
    
    def get_details(self):
        print("Department Name:", self.name)
        print("Department Manager:", self.manager.name)

#Class Company:

class Company:
    
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
    
    def get_details(self):
        print("Company Name:", self.name)
        for department in self.departments:
            print("Department Name:", department.name)
            print("Department Manager:", department.manager.name)
            print("Employees:")
            for employee in department.manager.employees:
                employee.get_details()

#Creating objects:

employee1 = Employee("John", 25, 10000, "IT")
employee2 = Employee("Michael", 22, 9000, "IT")
employee3 = Employee("Smith", 28, 11000, "Marketing")

manager1 = Manager("David", 30, 15000, "IT")
manager1.add_employee(employee1)
manager1.add_employee(employee2)

department1 = Department("IT", manager1)

manager2 = Manager("Ralph", 35, 16000, "Marketing")
manager2.add_employee(employee3)

department2 = Department("Marketing", manager2)

company1 = Company("ABC Pvt. Ltd.", [department, department])

#Printing details:

company1.get_details()
