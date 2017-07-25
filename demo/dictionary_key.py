# Duplication key
data = {"Key1": "first", "Key1": "second"}
print(data)

# Immutable key
data = { 1: "first",
         "two": "second",
         (1, 2): "third" }
print(data)

# Mutable key
data = { [1,2]: "first" }
