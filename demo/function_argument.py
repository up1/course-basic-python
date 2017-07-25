# Default and Keyword argument
def say_hi( name, age ):
    print("Hello %s, age = %d" %(name, age))

say_hi(name = "somkiat", age = 30)
say_hi(age = 30, name = "somkiat")

# Default argument
def say_hi2( name, age = 20 ):
    print("Hello %s, age = %d" %(name, age))

say_hi2(name = "somkiat")
say_hi2("somkiat")

# Variable-length argument
def sum(*numbers):
    result = 0
    for number in numbers:
        result = result + number
    print(result)
    return result

sum()
sum(1)
sum(1, 2)
sum(1, 2, 3)
sum(1, 2, 3, 4)
sum(1, 2, 3, 4, 5)
