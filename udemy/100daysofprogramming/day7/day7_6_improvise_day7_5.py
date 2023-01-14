import random
from words import word_list
from art import logo, stages
# from replit import clear

print(logo)
print('Guess a letter')

end_of_game = False
lives = 6

chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display.append(i.replace(i,'_')) #myway

w_list = []
while not end_of_game:
    guess = input().lower()
    w_list.append(guess)

    if guess in display:
        print(f"You've already guessed {guess}")
    if guess == '':
        print('You need to enter a letter')
    # if guess in w_list:
    #     print('You have already guessed this wrong letter!')
    
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i] #or display[i] = guess     
    if guess not in chosen_word or len(guess) > 1:
    # else: #else wont work here only if does
        lives -= 1
        print(f'Wrong! You have: {lives} lives left!')
        if lives == 0:
            end_of_game = True #myexplanation: This is like a flag statement instead of break
        print('You Lost!!')
        print(f'The word chosen was: {chosen_word}')
        # break   #myexplanation: Here break takes while loop exit and prints both print statements. Hence we need to try udemy way end_of_game
    print(display)
    
    
    if '_' not in display:
        end_of_game = True
        print('You Won!!!')
        print(f'The word chosen was: {chosen_word}')
        

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

#problem i saw was, t entering multiple lives lost lives but not r

