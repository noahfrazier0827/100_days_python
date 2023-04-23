num1 = int(input("x"))
num2 = int(input("y"))

def breaker(num1, num2):
    answer = num1 * num2
    num1 = answer
    answer = answer * num2
    breaker(num1, num2)

breaker(num1, num2)
