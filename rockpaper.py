while True:
    import random

    pc = random.randint(1,3)

    print("1. rock")
    print("2. paper")
    print("3. sciccors")
    print("4. exit")
    user = int(input("Pick a number\n"))

    if pc == 1:
        print("rock")
    elif pc == 2:
        print("paper")
    elif pc == 3:
        print("sciccors")
    else:
        print("oops!")

    print("VS.")

    if user == 1:
        print("rock")
    elif user == 2:
        print("paper")
    elif user == 3:
        print("sciccors")
    else:
        print("oops!")

    if user == 1 and pc == 3:
        print("You win.")
    elif user == 2 and pc == 1:
        print("you win.")
    elif user == 3 and pc == 2:
        print("You win.")
    elif user == pc:
        print("Tie.")
    else:
        print("you lose.")

    if user == 4:
        break