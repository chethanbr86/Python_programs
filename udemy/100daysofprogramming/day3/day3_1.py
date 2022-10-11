#myown
print('Welcome to treasure Island!')
way1 = input('you are at a cross road, do you wanna move "left" or "right": ').lower()
print('your input is',way1)
while way1:
    if way1=='left': 
        print('You came to a lake. There is an island in the middle of lake.')
        way2 = input('Do you wanna "wait" for boat or "swim" across: ').lower()  #Do something if there is any other input
        print('your input is',way2)
        while way2:
            if way2=='wait': 
                print('You arrive at island unharmed. There is a house with 3 doors. One "Red", one "Yellow" and one "Blue".')   
                way3 = input('Which color do you choose?: ').lower() #Do something if there is any other input
                print('your input is',way3)     
                while way3: 
                    if way3=='blue': 
                        print('You enter a romm of Beasts. Game Over!')
                    elif way3=='red':
                        print('You enter a room of Fire. Game Over!')
                    elif way3=='yellow':
                        print('You Won!')
                    else:
                        print('Select either of 3 gems.')
                    break
            elif way2=='swim':
                print('You are eaten by crocodile. Game Over!')
            else:
                print('Input must either be wait or swim.')
            break
    elif way1=='right':
        print('You fell in a hole. Game Over!')
    else:
        print('Input must either be left or right.')  
    break

#udemy solution
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# #Write your code below this line 👇

# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")