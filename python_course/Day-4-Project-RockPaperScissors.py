rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print('''Welcome to the RPS Tournament!!!
You are the first challenger!
Let's Play!!!''')
import random
weapons = [rock, paper, scissors]
choice = input("Choose your weapon! Rock? Paper? Scissors? ").lower()
if choice == "rock":
    player_choice = weapons[0]
elif choice == "paper":
    player_choice = weapons[1]
elif choice == "scissors":
    player_choice = weapons[2]
else:
    print("You lose! Pick a correct weapon!")
    exit()

print(f"Player chose:\n{player_choice}\n")

computer_choice = random.choice(weapons)
print(f"Computer chose:\n{computer_choice}\n")

w = "You Win!"
l = "You Lose!"

if player_choice == rock and computer_choice == scissors:
    print(w)
elif player_choice == scissors and computer_choice == rock:
    print(l)

if player_choice == scissors and computer_choice == paper:
    print(w)
elif player_choice == paper and computer_choice == scissors:
    print(l)

if player_choice == paper and computer_choice == rock:
    print(w)
elif player_choice == rock and computer_choice == paper:
    print(l)

if player_choice == computer_choice:
    print("Draw")
