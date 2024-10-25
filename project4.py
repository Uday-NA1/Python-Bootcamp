import random

game_choices = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

computer_choice = random.randint(0, 2)
print(f"Computer Chose:")
print(game_choices[computer_choice])

if computer_choice == 0 and user_choice == 2:
    print("You Win!")

elif computer_choice > user_choice:
    print("You Lose!")

elif computer_choice == user_choice:
    print("It's a draw!")

else:
    print("You typed an invalid number. You lose!")