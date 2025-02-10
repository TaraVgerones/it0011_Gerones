firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
age = input("Enter Age: ")
fullName = firstName + ' ' + lastName
sliceName = firstName[:3]
print()
message = "Hello, {fName}! Welcome. You are {Age}  years old".format(fName = sliceName, Age=age)
print("Full name: ", fullName)
print("Sliced name: ", sliceName)
print("Greeting Message: ", message)