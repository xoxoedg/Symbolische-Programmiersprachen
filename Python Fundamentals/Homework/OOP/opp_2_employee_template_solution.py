"""
Exercise 2: Employee class [6 points]

1. Complete Employee class with docstrings [1 point]
  Properly defined Employee class with correct attributes and methods.
  Every method has a documentation string that describes its functionality.

2. Main application with various employees [1 point]
  Successfully creates multiple employee instances.
  Demonstrates manipulation of employee objects using class methods.

3. Department dictionary creation and printing [1 point]
  Constructs a department dictionary that associates department names with lists or sets of employees.
  Prints each employee's name preceded by their respective department in the format <department> <employee name>.
  Departments: e.g., HR, Engineering

4. Extend the Employee class with salary attribute and give_raise() method [1 point]
  Successfully added a salary attribute to the Employee class.
  Implemented a give_raise(self, amount) method that correctly increases an employee's salary by the specified amount.

5. Extend the Employee class with calculate_bonus() method [1 point]
  Added a method calculate_bonus(self) that calculates an annual bonus as 10% of the employee's salary.
  Demonstrated the calculation and display of bonuses in the main application.

6. Extend the Employee class with the attribute best_employee and the  method make_employee_of_the_month(self) [1 point]
  Successfully added a best_employee attribute to the Employee class (with default value False).
  Implemented a make_employee_of_the_month(self) method that correctly changes the value of best_employee to True for an object.
"""


class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    name : str
        Name of the employee
    department : str
        Department where the employee works
    age : int
        Age of the employee
    salary : float
        Salary of the employee
    best_employee : bool
        employee of the month True/False

    Methods
    -------
    set_department(new_department):
        Change the department of the employee.
    give_raise(amount):
        Increase the salary by the given amount.
    calculate_bonus():
        Calculate annual bonus as 10% of the salary.
    make_employee_of_the_month():
        Change best_employee attribute to True
    """

    def __init__(self, name, department, age, salary, best_employee=False):
        self.name = name
        self.department = department
        self.age = age
        self.salary = salary
        self.best_employee = best_employee

    def set_department(self, new_department):
        """Change the department of the employee."""
        self.department = new_department

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Department: {self.department}, Salary: ${self.salary}, "
                f"Employee of the month: {self.best_employee}")

    def give_raise(self, amount):
        """Increase the salary by the given amount."""
        self.salary += amount

    def calculate_bonus(self):
        """Calculate annual bonus as 10% of the salary."""
        return self.salary * 0.10
    
    def make_employee_of_the_month(self):
        self.best_employee = True


if __name__ == "__main__":
    # Create Employee objects
    emp1 = Employee("Alice", "HR", 30, 50000)
    emp2 = Employee("Bob", "Engineering", 25, 55000)
    emp3 = Employee("Charlie", "HR", 28, 52000)
    emp4 = Employee("David", "Engineering", 32, 57000)

    # Manipulate Employee objects
    emp1.set_department("Engineering")
    emp2.give_raise(5000)
    print(emp1)  # Showcasing __str__ method
    print(emp2)  # Showcasing updated salary after raise

    # Create department dictionary
    departments = {
        "HR": [emp3],
        "Engineering": [emp2, emp1, emp4]
    }

    # Print department and employee name for each employee in the dictionary
    for dept, employees in departments.items():
        for emp in employees:
            print(f"{dept} - {emp.name}")

    # Calculate and display bonuses
    for emp in [emp1, emp2, emp3, emp4]:
        bonus = emp.calculate_bonus()
        print(f"{emp.name}'s annual bonus is: ${bonus:.2f}")
