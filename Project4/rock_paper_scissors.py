import random

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

results_list = [rock,paper,scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(results_list[player_choice])

computer_choice = int(random.randint(0,2))
print("Computer Chose:" )
print(results_list[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You Lose incorrect value")
elif player_choice == 2 and computer_choice == 0:
    print("You Lose")
elif player_choice == 0 and computer_choice == 2:
    print("You Win")
elif player_choice > computer_choice:
    print("You Win")
elif player_choice < computer_choice:
    print("You Lose")
elif player_choice == computer_choice:
    print("It's a Draw")
