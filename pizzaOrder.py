print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pay = 0
if size == "S":
    pay = 15
elif size == "M":
    pay = 20
elif size == "L":
    pay = 25
else:
    print("Please put S, M, or L.")

if add_pepperoni == "Y" and size == "S":
    pay += 2
elif add_pepperoni == "Y" and size == "M":
    pay += 3
elif add_pepperoni == "Y" and size == "L":
    pay += 3
elif add_pepperoni == "N":
    pay = pay
else:
    print("Please select Y or N.")

if extra_cheese == "Y":
    pay += 1
    print(f"Your final bill is: ${pay}.")
else:
    print(f"Your final bill is: ${pay}.")
