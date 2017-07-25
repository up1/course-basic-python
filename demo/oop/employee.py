class Employee:
    class_variable = 1

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_data(self):
        return "Data of %s" % self.name

    def __str__(self):
        return "%d : %s : %d" %(self.id, self.name, self.age)


# Create object and call variable
emp1 = Employee(1, "Somkiat", 30)
print(emp1.get_data())

print(Employee.class_variable)


# Access attributes
emp1.id = 111
emp1.name = "New name"
emp1.age = 100

print(str(emp1))
