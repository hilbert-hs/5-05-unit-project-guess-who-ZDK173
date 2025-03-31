import random
import Colors
import Characters
################### Character Dictonary ################### 
charactersZ = (Characters.characterZ)

charactersP = (Characters.characterP)

characters = (Characters.characters)

Zombies = list(charactersZ.keys())
Plants = list(charactersP.keys())

PVZ = random.randint(1,2)

if PVZ == 2:
  Secret_Cht = random.choice(Zombies)
else:
  Secret_Cht = random.choice(Plants)

##################### Game Functions ###################### 
print()

def list_characters(dict, dict2):
  for zom in dict:
    print(f"{Colors.purple}Side {zom}{Colors.reset} is from {Colors.yellow}Game {dict[zom]['Game']}{Colors.reset}, is in the {Colors.red}{dict[zom]['Class']} Class{Colors.reset}, has {Colors.lightcyan}{dict[zom]['Variants']} Variants{Colors.reset} and has {Colors.green}{dict[zom]['Health']} Health.{Colors.reset}")
    print()
  for zom in dict2:
    print(f"{Colors.green}Side {zom}{Colors.reset} is from {Colors.yellow}Game {dict2[zom]['Game']}{Colors.reset}, is in the {Colors.red}{dict2[zom]['Class']} Class{Colors.reset}, has {Colors.lightcyan}{dict2[zom]['Variants']} Variants{Colors.reset} and has {Colors.green}{dict2[zom]['Health']} Health.{Colors.reset}")
    print()

def ask(trait,):
  if trait == 'class':
   trait = 'Class'
  elif trait == 'game': 
    trait = 'Game'
  elif trait == 'variants':
    trait = 'Variants'
  elif trait == 'health':
    trait = 'Health'
  elif trait == 'side':
    trait = 'Side'
  print()
  print(f'The {trait} of the secret character is {characters[Secret_Cht][trait]}')
  print()

def guess(user_guess):
  if user_guess != Secret_Cht:
    return(False)
  else:
    print("You are Right. You Win!")
    print()
    return(True)

def help():
  print("Actions:   Ask   Guess   Quit")
  print()

def quit():
  print(f'The Mystery Character was {Secret_Cht}.')


####################### Game Loop ######################## 

list_characters(charactersZ, charactersP)

Win = False

while Win == False:
  Action = input("What would you like to do? ")
  print()
  if Action == "ask":
    trait = input("What trait would you like to know? ")
    ask(trait)
  elif Action == "guess":
    G = input("Who do you think it is? ")
    print()
    Win = guess(G)
  elif Action == "help":
    help()
  elif Action == "quit":
    quit()
    Win = True