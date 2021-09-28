"""
Simple script to calculate your pokémon's IV percentage.
Input the attack IV, defense IV, and HP/stamina IV, and you will get a rounded percentage.
If you so choose, you can retry with another pokémon by pressing "y" or "n" when given the "Try again? (y/n)" prompt.
"""

import os

#Clears the previous code output if any.
os.system('cls' if os.name == 'nt' else 'clear')

#This makes it so that when the function is called, the user can only enter in numbers between 0 and the number stated
def inputRestriction(num):
  while True:
    try:
      a = int(input())
    
    #If input is not a number:
    except ValueError:
      print(f"\nSorry, I didn't understand that. Please enter a number.")
      continue

    #If input is outside of set boundaries (0-<stated number>)
    if not (0 <= a <= num):
      print(f"\nPlease choose out a number from 0 and {num}")
    
    #If both requirements are met (a real number, and a number within range), the script will continue.
    else:
      break

  return a

#Collecting Pokemon IV Values
def PerfectionFinder():
  print(f"\nEnter Attack value (0-15): ")
  attack = inputRestriction(15)

  print(f"\nEnter Defense value (0-15): ")
  defense = inputRestriction(15)

  print(f"\nEnter HP value (0-15): ")
  stamina = inputRestriction(15)

  IVCollection = attack + defense + stamina
  perfection = (IVCollection / 45) * 100
  result = round(perfection)

  print("\nYour pokémon is " + str(result) + "% perfect.\n")

  #To try again
  r = input("Try again? (y/n)\n")
  if r == "yes" or r == "y" or r == "":
    os.system('cls' if os.name == 'nt' else 'clear')
    PerfectionFinder()
  if r == "no" or r == "n":
    print("\nTerminating Script.")

#Calls the function
PerfectionFinder()
