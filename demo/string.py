input = "Hello World"

# Slice
print(input[0])
print(input[1])

# Range slice
print(input[0:2])
print(input[0:])
print(input[:5])

for c in input:
    print(c)

if "z" in input:
    print("Found data")
else:
    print("Not Found data")
