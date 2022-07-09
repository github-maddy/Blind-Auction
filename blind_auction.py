
from turtle import clear
import art
print(art.logo)
auction = {}
highest = 0
repeat = True
while repeat == True:
  n = input("Enter your name : ")
  a = int(input("Enter your bid amount : "))

  if a > highest:
    highest = a
  auction[n]=a
  value = list(auction.values())
  key = list(auction.keys())
  position = value.index(highest)
  highest_name = (key[position])
  again = input("Is there any other bidders (Yes or No) : ").lower()
  clear()
  if again == 'no':
    repeat = False
    print(f"{highest_name}'s bid is highest {highest}")
  
  