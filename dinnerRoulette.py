# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_count = len(names)
dinner = random.randint(0, name_count -1)
print(f"{names[dinner]} is paying the bill!")