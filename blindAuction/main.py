from replit import clear
from art import logo


flag = True
participants = {}



def find_highest_bidder(bidding_record):
  highest = 0 
  winner = ""
  for i in bidding_record:
    value = bidding_record[i]
    if value > highest:
      highest = value
      winner = i
  print(f"The winner is {winner} with a bid of ${highest}")

print(logo)
print("Welcome to the secret auction program.")

while flag:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  participants[name] = bid
  more_bid = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()

  if more_bid == "no":
    flag = False 
    find_highest_bidder(participants) 
  elif more_bid == "yes":
    clear()
    
  

  
