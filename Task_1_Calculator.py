def add(a, b):
    #This function adds two numbers
    return a + b

def subtract(a, b):
    #This function subtracts two numbers
    return a - b

def multiply(a, b):
    #This function multiplies two numbers
    return a * b

def divide(a, b):
    #This function divides two numbers
    if b == 0:
        return "Error! can't divide by Zero."
    else:
        return a / b

while True:
    #Take input from the user
    num1 = float(input("\nEnter First number:"))
    num2 = float(input("\nEnter Second number:"))
    op = input("\nEnter Operation( +, -, *, / ):")

    #Perfrom the Calulation
    if op == '+':
        print(f"\n{num1} + {num2} = {add(num1,num2)}")

    elif op == '-':
        print(f"\n{num1} - {num2} = {subtract(num1,num2)}")
        
    elif op == '*':
        print(f"\n{num1} * {num2} = {multiply(num1,num2)}")
        
    elif op == '/':
        print(f"\n{num1} / {num2} = {divide(num1,num2)}")

    else:
        print("Invalid Input")
        


