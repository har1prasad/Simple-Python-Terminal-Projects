import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

biddlist = {}
tocontinue = "yes"
high = 0

while tocontinue != "no":
  clear_screen()
  name = input("What is your Name ?: ")
  amount = int(input("How muc is your bid amount ?: $"))

  biddlist[name] = amount
  tocontinue = input("Are there any other's to bid ? 'yes' or 'no': ")

for i in range(len(biddlist)):
  for key in biddlist:
    if high < biddlist[key]:
      high = biddlist[key]
      bidd=key
      

if tocontinue =="no":
  clear_screen()
  print(f"the highest bidder is {bidd}")

  """This is how a docstring will be in a function or class of python."""
