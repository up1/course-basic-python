#Create list
myList = []
myList.append(1)
myList.append(2)
myList.append("Three")

#Accessing Values in Lists
print(myList)
print(myList[0])
print(myList[1])
print(myList[2])

#Iterate myList
for data in myList:
    print(data)

#Update data in list
myList[0] = "One"
print(myList)

#Delete data in list
del myList[0]
print(myList)
