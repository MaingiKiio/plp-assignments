# basic calculator programme


def calculator(): #use a function calculator
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0: #verify if the number to be divided is zero
                print("Math Error!: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()