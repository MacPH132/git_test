# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
c1 = year % 4
c2 = year % 100
c3 = year % 400

if c3 != 0:
    if c2 != 0:
        if c1 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")