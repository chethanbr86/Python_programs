#myown
print('Welcome to treasure Island!')
way1 = input('you are at a cross road, do you wanna move left or right: ').lower()
print('your input is',way1)
while way1:
    if way1=='left':
        print('You came to a lake. There is an island in the middle of lake.')
        way2 = input('Do you wanna wait for boat or swim across: ').lower()
        print('your input is',way2)
        while way2:
            if way2=='wait':
                print('You arrive at island unharmed. There is a house with 3 doors. One Red, one Yellow and one Blue.')   
                way3 = input('Which color do you choose?: ').lower()
                print('your input is',way3)     
                while way3:
                    if way3=='blue':
                        print('You enter a romm of Beasts. Game Over!')
                    elif way3=='red':
                        print('You enter a romm of Ghouls. Game Over!')
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