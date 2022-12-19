operatA = 3
operatB = 2
add = operatA + operatB
print(add)
print(f'Add result: {add}') # mejor forma de imprimir informacion, ya que sirve para imprimir textos mas largos con varias variables

# operador de asignación
myVariable = 10   # asigamos un valor de 10 a myVariable
# operador de reasignación
myVariable+= 2
print(myVariable)


# operadores de comparacion
operatA = 2
operatB = 5
result = operatA == operatB
print(result)

# Operadores logicos

a = True
b = True
result = a and b
print(result)

# EXAMPLES
# Numero par o impar
number = int(input("Insert a number please: "))
if number % 2 == 0:
    print(f'{number} is par')
else:
    print(f'{number} is not par')

# Mayor de edad

age = int(input("Inster your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You aren't an adult")

# Valor entre un rango
number = int(input("Type a number: "))
rangeA = 1
rangeB = 20
if (number > 1 and number < 20):
    print(f'{number} is in range (1 - 20)')
else:
    print(f'{number} is not in range')

print("Proporciona los siguientes datos del libro:")
id = int(input("id: "))
price = int(input("price: "))
sending = input("Es envio gratuito? (Yes/No): ")


