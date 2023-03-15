print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

newName1 = name1.lower()
t =newName1.count("t")
r =newName1.count("r")
u = newName1.count("u")
e = newName1.count("e")
num1 = t + r + u + e

newName2 = name2.lower()
l = newName2.count("l")
o = newName2.count("o")
v = newName2.count("v")
e2 = newName2.count("e")
num2 = l + o + v + e2

print(f"Your score is {num1}{num2} ")