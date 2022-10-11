import random
from words import word_list
from art import logo, stages

print(logo)
#myexplanation: There has to be 7 lives because of 7 drawings and lives not dependent on length of word
# word_list = ["ardvark", "baboon", "camel"]

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
end_of_game = False
lives = 6

chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display.append(i.replace(i,'_')) #myway

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

# while '_' in display: #myway #myexp: if you use this, u can use break along with end_of_game else with another while statement break is not required
while not end_of_game:
    guess = input().lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i] #or display[i] = guess     
    if guess not in chosen_word or len(guess) != 1:
    # else: #else wont work here only if does
      lives -= 1
      print('Wrong! You have:', lives, 'lives left!')
      if lives == 0:
        end_of_game = True #myexplanation: This is like a flag statement instead of break
        print('You Lost!!')
        print('The word chosen was: ', chosen_word)
        # break   #myexplanation: Here break takes while loop exit and prints both print statements. Hence we need to try udemy way end_of_game
    print(display)
    
    
    if '_' not in display:
      end_of_game = True
      print('You Won!!!')
      print('The word chosen was: ', chosen_word)
        

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

