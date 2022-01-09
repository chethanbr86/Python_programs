print('Welcome to treasure Island!')
way1 = input('you are at a cross road, do you wanna move left or right: ')
print('your input is',way1)

if way1=='left':
    print('You came to a lake. There is an island in the middle of lake.')
elif way1=='right':
    print('Right')
else:
    print(input('Input must either be left or right: '))

way2 = input('Do you wanna wait for boat or swim across: ')
print('your input is',way2)

if way2=='wait':
    print('You arrive at island unharmed. There is a house with 3 doors. One Red, one Yellow and one Blue.')
elif way2=='swim':
    print('Swim')
else:
    print('Input must either be wait or swim')

way3 = input('Which color do you choose?: ')
print('your input is',way3)

if way3=='Blue':
    print('You enter a romm of Beasts. Game Over!')
elif way3=='Red':
    print('You enter a romm of Ghouls. Game Over!')
elif way3=='Yellow':
    print('You Won!')
else:
    print('Select either of 3 gems.')