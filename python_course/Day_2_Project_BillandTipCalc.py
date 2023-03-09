#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Bill and Tip Calculatorinator")

tbill = input("What is the total bill? ")
b = float(tbill)

ptip = input("What percentage tip would you like to give? 10, 12, or 15? ")
ftip = float(ptip)
tip = ftip / 100 + 1

n = input("How many people to split the bill? ")
num_peeps = float(n)

share = (b * tip) / num_peeps
formatted_share = "{:.2f}".format(share)
print(f"Each person should pay: ${formatted_share}")