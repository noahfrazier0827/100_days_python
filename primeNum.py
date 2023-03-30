
# n = int(input("Check this number: "))
# prime_checker(number=n)

# n = int(input("insert number\n"))

def prime_checker(number):
    y = 0
    for x in range(1, number + 1):
        if number % x == 0:
            y += 1
            
    if y == 2:
        print("prime")
    else:
        print("not prime")

prime_checker(int(input("insert number\n")))
