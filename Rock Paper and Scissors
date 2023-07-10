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

#code for rock , paper and scissors
game_image = [rock,paper,scissors]
user_choice = int(input('What is your choice Type 0 for "rock", 1 for "paper" or 2 for "scissors"\n'))
print(game_image[user_choice])
computer_choice = random.randint(0,2)
print(game_image[computer_choice])
if user_choice >= 3 and user_choice < 0:
  print("You've entered the invalid number, You Lose")
elif user_choice == 0 and computer_choice == 2:
  print("You Win")
elif computer_choice == 0 and user_choice == 2:
  print("You Lose")
elif computer_choice > user_choice:
  print("You Lose")
elif user_choice > computer_choice:
  print("You Win")
elif user_choice == computer_choice:
  print("It's a Draw")
