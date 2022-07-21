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

end_of_game = False
# lives = len(chosen_word)  #myway won't work since there are seven stages of lives
lives = 7
print(f'You have {lives} lives!')
while not end_of_game:  #'_' in display: #myway - while loop is not working, hence doing udemy way 
    guess = input().lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i] #or display[i] = guess    

    if guess not in chosen_word[i]:        
        lives = lives - 1             
        if lives == 0:
            end_of_game = True
            print('you Lost')     
    print(lives)   
    print(display)

    if '_' not in display:
        end_of_game = True
        print('You  Won!!!')
        

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

