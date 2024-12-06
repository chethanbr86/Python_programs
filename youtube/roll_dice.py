#Rolling the dice until times or target is reached 
import random

#myway - works for 1 player with target and numer of times they roll 
# total = 0
# times = int(input())
# target = int(input())

# for _ in range(times):
#     num = random.randint(1,6)
#     # print(f'num: {num}')
#     if num == 1 or total >= target:
#         total = 0
#         print(f'out, num1: {num}, total: {total}')
#         break
#     else:
#         total = total + num
#         print(f'not out, num2: {num}')
#     print(f'total: {total}')

#otherway - includes number of players with target and can roll as many times as they say yes or until they win
def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input('Enter number of players (2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Number of players should be between 2 and 4')
    else:
        print('Only digits allowed')

player_scores = [0 for _ in range(players)] #initializing all players with 0 score at beginning*
print(player_scores)