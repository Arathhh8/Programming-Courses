myVariable = "Hello world from Python"

print(myVariable)

myVariable = 2
print(myVariable)

myVariable = 2.2222
print(myVariable)

# add two numbers

x = 10
y = 20
z = x + y
print(x + y)
print(z)

# memory direction

print("x: ", id(x))

# data types

x: int = False  # is only for visual help
print(x)
print(type(x))  # return x's type variable

# Strinf manage

myFavoriteBand = "Pink Floyd"
comment = "the best rock band"
print("My forite band is: " + myFavoriteBand + " " + comment)

# Bool type
myVariable = True
print(myVariable)

myVariable = 3 > 2 #is a question "3 is bigger than 2?"
print(myVariable)

if myVariable:
    print("Result is true")
else:
    print("Result is false")

# procesar entrada de usuario

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
result = num1 + num2
print("Result = ", result)

#Califica tu día

result = input("How was your day?: ")
print("My day was of: ", result)