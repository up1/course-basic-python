# Create dictionary
empty = {}
employee = {"firstname": "Somkiat",
            "lastname": "Pui",
            "age": 30}

print(employee)

#Iterate
for key, value in employee.items():
    print("%s : %s" %(key, value))

# Access value in dictionary
print(employee["firstname"])
print(employee["lastname"])
print(employee["age"])

# Update data in dictionary
employee["firstname"] = "New name"
employee["age"] = 20

print(employee)

# Delete
del employee["firstname"]
print(employee)

employee.clear()
print(employee)

del employee
print(employee)
