def add(*numbers):
    result = 0
    for number in numbers:
        result = result + number
    print(result)
    return

add()
add(1)
add(1,2)
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5)

def hello(name, age = 20):
    result = "Hello " + name
    print("%s, age=%d" %(result, age))

hello("Somkiat")
hello("Somkiat", 30)
hello(name="Somkiat", age=30)
hello(age=30, name="Somkiat")
