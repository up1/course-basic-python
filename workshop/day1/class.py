class Employee:
    __counter = 1
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Your name is " + self.name

emp = Employee("somkiat")
print(emp._Employee__counter)
