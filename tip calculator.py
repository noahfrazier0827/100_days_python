#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line 

number_of_People = input("How many people are there?\n")
bill = input("how much was the bill?\n")
tip_Percent = input("what percent of tip do you want to pay?\n")

pay_Per = float(bill)/float(number_of_People)
tip_Per = pay_Per * float(tip_Percent)
final_Pay = pay_Per + float(tip_Per)

final_pay_Rounded = round(final_Pay, 2)

print(final_pay_Rounded)
