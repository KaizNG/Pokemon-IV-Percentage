"""
Simple script to calculate your pokémon's IV percentage.
Input the attack IV, defense IV, and HP/stamina IV,
and you will get a rounded percentage.
"""

import os

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
  #Clears the previous code output if any.
  os.system('cls' if os.name == 'nt' else 'clear')

  print("\nEnter Attack value (0-15): ")
  attack = inputRestriction(15)

  print("\nEnter Defense value (0-15): ")
  defense = inputRestriction(15)

  print("\nEnter HP value (0-15): ")
  stamina = inputRestriction(15)

  result = round(((attack + defense + stamina) / 45) * 100)

  print("\nYour pokémon is {}% perfect.\n".format(result))

  #To try again
  x = input("Try again? (Enter anything to continue, Enter \"n\" to stop)\n").lower()
  if x == "n":
    print("\nTerminating Script.")
    quit()
  else:
    PerfectionFinder()

#Calls the function
PerfectionFinder()
