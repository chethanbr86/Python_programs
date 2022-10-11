import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for i in chosen_word:
    display.append(i.replace(i,'_')) #myway
    # display += '_'  #udemy
# print(display)

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters 
# in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

# end_of_game = False   #udemy way

while '_' in display: #myway
# while not end_of_game:
    guess = input().lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i] #or display[i] = guess     
    print(display)
print('You Won!')
    # if '_' not in display:
    #     end_of_game = True
    #     print('You Win')

#Here both my way and udemy way works