import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for i in chosen_word:
    display.append(i.replace(i,'_')) #myway

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

lives = len(chosen_word)
print(lives)
while '_' in display: #myway
    guess = input().lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i] #or display[i] = guess            
    print(lives)
    print(display)

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

if '_' not in display:
    print('You  Won!!!')
else:
    print('You lost!)')

#not solved yet

