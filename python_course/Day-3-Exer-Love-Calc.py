    # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n = name1.lower() + name2.lower()
T = n.count("t")
R = n.count("r")
U = n.count("u")
E = n.count("e")
L = n.count("l")
O = n.count("o")
V = n.count("v")

tenth = T + R + U + E
ones = L + O + V + E
score = int(str(tenth) + str(ones))

if score <= 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")