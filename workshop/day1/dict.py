employee = {
    "id": 1,
    "name": "Somkiat"
}

print(employee["id"])
print(employee["name"])

for key in employee.keys():
    print("%s => %s" %(key, employee[key]))

for key, value in employee.items():
    print("%s => %s" %(key, value))
