year = int(input("Which year do you want to check? "))

yearA = year % 4
yearB = year % 100
yearC = year % 400

if yearA == 0 and yearB > 0:
    yearC == 0
    print("Leap year.")
else:
    print("Not leap year.")


