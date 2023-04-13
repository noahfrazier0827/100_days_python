
def prime_checker(num):
    y = 0
    for x in range(1, num + 1):
        if num % x == 0:
            y += 1
            
    if y == 2:
        print("prime")
    else:
        print("not prime")

prime_checker(int(input("insert number\n")))
