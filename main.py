# random
from random import randint, choice

  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
# print("random")
# first_random = randint(1,50)
# print(first_random)
dice1 = randint(1,6)
dice2 = randint(1,6)
dice3 = randint(1,6)
dice4 = randint(1,6)
dice5 = randint(1,6)
dice6 = randint(1,6)

my_gamble = dice1 + dice2 + dice3 + dice4 + dice5 + dice6
# if my_gamble % 2 == 1:
#   print("You almost won")
# elif my_gamble == 8:
#   print("Roll again")
# elif my_gamble > 12 and my_gamble < 18:
#   print("You lost")
# else:
#   print("you win")






# dictionary1 = {}
# color = ['blue', 'red', 'green', 'turquoise', 'purple']
# myRandom = choice(color)
# print(myRandom)
myCharacters = ['Rogue', 'Elf', 'Knight', 'Ninja', 'Samurai']
for character in myCharacters:
  if my_gamble == character[0]:
    print(character)
  else:
    print(my_gamble)
  # from random import shuffle
  # # This shuffles the list "in-place" meaning it won't return
  # # anything, instead it will effect the list passed
  
  
  # shuffle(mylist)
  # mylist
  
  # [40, 10, 100, 30, 20]
  # from random import randint
  # # Return random integer in range [a, b], including both end points.
  # randint(0,100)
  # 25
  
  
  # # Return random integer in range [a, b], including both end points.
  # randint(0,100)
  # 91
  
  
  
  ################################################random in python#################################################
  # Random Practice #1
  # Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.
  
  
  # Random Practice #2
  # Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.
  
  
  # Random Practice #3
  # Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.
  
  # names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
  
  
