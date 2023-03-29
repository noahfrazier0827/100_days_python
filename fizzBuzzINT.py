for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 >= 1:
        print("Fizz")
    elif num % 3 >= 1 and num % 5 == 0:
        print("Buzz")
    else:
        print(num)