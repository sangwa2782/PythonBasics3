class Employee:
     def __init__(self, name, salary):
         self.name = name
         self.salary = salary

     def getSalary(self):
         print(self.salary)


rohan = Employee("Rohan", "24556")

rohan.getSalary()

harry = Employee("Harry", "653254")

harry.getSalary()