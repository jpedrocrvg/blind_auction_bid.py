from replit import clear
from art import logo
print(logo)

bid_type = {}
continues = True

while continues:
  name = input('What is you name? ')
  bid = input('What is your bid type? $')
  bid_type[name] = bid
  asks = input('Is there another user who wants to type? Y or N ')
  if asks == 'Y':
    continues = True
    clear()
  else:
    continues = False

highest_bidder = None
highest_bid = None

for name, bid in bid_type.items():
    if highest_bid is None or bid > highest_bid:
        highest_bidder = name
        highest_bid = bid

print("The highest bidder is:", highest_bidder)
print("Their bid type is: $", highest_bid)
