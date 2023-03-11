#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random
choice = input("Heads or Tails? ").lower()

if choice == "heads":
    num = 0
elif choice == "tails":
    num = 1
else:
    print("please type heads or tails.")

coin = random.randint(0,1)

if coin == 0:
    print("Heads")
else:
    print("Tails")

if num == coin:
    print("You got it right!")
else:
    print("You got it wrong!")
