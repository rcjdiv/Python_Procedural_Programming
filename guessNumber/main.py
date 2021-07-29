#using blocks
# hard 10 attemps
# easy 5 attemps
# you have _ attempts remaining to guess the number
#Make a guess:
#Guess again
# You got it! the answer was _
# You've run out of guesses you lose
import random
easy = 10
hard = 5

def checker(your_guess, the_answer, your_turns):
  if your_guess == the_answer:
    return print(f"You got it! the answer was {the_answer}")

  elif your_guess > the_answer:
    print("Too High")
    return your_turns - 1

  elif your_guess < the_answer:
    print("Too Low")
    return your_turns - 1

def difficulty(your_choice):
  if your_choice == "easy":
    return easy
  if your_choice == "hard":
    return hard

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(0, 100)

  choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  turns = difficulty(choice)

  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))

    turns = checker(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses you lose")
      return
    elif guess != answer:
      print("Guess Again")


game()
