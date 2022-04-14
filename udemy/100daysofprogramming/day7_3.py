import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for i in chosen_word:
    display.append(i.replace(i,'_')) #myway
    # display += '_'  #udemy
print(display)

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters 
# in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

guess = input().lower()
for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = chosen_word[i] #or display[i] = guess
        print('correct')
    else:
        print('wrong')
print(display)