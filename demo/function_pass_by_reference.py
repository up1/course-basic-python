def try_to_change(data):
    data[2] = 300
    return

input = [0, 0, 0]
print("Before ", input)
try_to_change(input)
print("After ", input)
