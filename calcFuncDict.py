def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Whats the first number?\n"))
    for symbol in operations:
        print(symbol)
        should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation.\n")

        num2 = float(input("Whats the next number?\n"))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1}{operation_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\n") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
