###FUNCTIONS###

def guessEasy():
    import random
    pcnum = random.randint(1,101)
    lives = 10

    while True:
        guess = int(input("What number do you want to guess?\n"))
        
        higher = False
        lower = False
        if guess > pcnum:
            higher = True
        elif guess < pcnum:
            lower = True

        difference = pcnum - guess
        if difference <= 0:
          difference = abs(difference)

        if pcnum != guess:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
            
        if difference >= 20 and higher:
            print("Way too high.")
        elif difference >= 10 and higher:
            print("Too high")
        elif difference >= 1 and higher:
            print("Lower.")

        if difference >= 20 and lower:
            print("Way too low.")
        elif difference >= 10 and lower:
            print("Too low")
        elif difference >= 1 and lower:
            print("Higher.")

        if pcnum == guess:
            print(f"The number was {pcnum}! You win.")
            break
        if lives == 0:
            print("Game Over.")
            break

def guessHard():
    import random
    pcnum = random.randint(1,101)
    lives = 5

    while True:
        guess = int(input("What number do you want to guess?\n"))
        
        higher = False
        lower = False
        if guess > pcnum:
            higher = True
        elif guess < pcnum:
            lower = True

        difference = pcnum - guess
        if difference <= 0:
          difference = abs(difference)

        if pcnum != guess:
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
            
        if difference >= 20 and higher:
            print("Way too high.")
        elif difference >= 10 and higher:
            print("Too high")
        elif difference >= 1 and higher:
            print("Lower.")

        if difference >= 20 and lower:
            print("Way too low.")
        elif difference >= 10 and lower:
            print("Too low")
        elif difference >= 1 and lower:
            print("Higher.")

        if pcnum == guess:
            print(f"The number was {pcnum}! You win.")
            break

        if lives == 0:
            print("Game Over.")
            break

###START OF CODE###

print("welcome to the number guessing game.")
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard', or type 'x' to exit\n")

    if difficulty == "easy":
        guessEasy()
    elif difficulty == "hard":
        guessHard()
    elif difficulty == "x":
        break
    else:
        print("Please select a valid option.")