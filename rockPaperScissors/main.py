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
game_images = [rock, paper, scissors]
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game_images[answer])

comp= random.randint(0, 2)
print(f"Computer chose")
print(game_images[comp])

if answer >= 3 or answer < 0:
  print("You typed an invalid number, Game over!")
elif answer == 0 and comp == 2:
  print("You win!")
elif comp == 0 and answer == 2:
  print("You lose!")
elif comp > answer:
  print("You lose!")
elif answer > comp:
  print("You win!")
elif answer == comp:
  print("Its a draw")
