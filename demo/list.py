# Create List
empty = []
numbers = [1, 2, 3, 4, 5]
string = ["H", "e", "l", "l"]
mix = [1, 2, "three", True]

for data in mix:
    print(type(data))

# Access List
mix = [1, 2, "three", True]
print(mix[0])
print(mix[1])
print(mix[1:3])

# Update
mix[0] = "1"
print(mix)

# Delete
del mix[0]
print(mix)

# Basic operation
print(len(mix))
mix.append("New")
print(len(mix))
print(mix)

# Range slice
numbers = [1, 2, 3, 4, 5]
print(numbers[0:3])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
