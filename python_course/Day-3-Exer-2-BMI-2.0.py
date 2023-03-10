# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
n = round(bmi)

if n <= 18.5:
    print(f"Your BMI is {n}, you are underweight.")
elif n > 18.5 and n <= 25:
    print(f"Your BMI is {n}, you have a normal weight.")
elif n > 25 and n <= 30:
    print(f"Your BMI is {n}, you are slightly overweight.")
elif n > 30 and n <= 35:
    print(f"Your BMI is {n}, you are obese.")
else:
    print(f"Your BMI is {n}, you are clinically obese.") 
