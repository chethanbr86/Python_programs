#Rolling the dice until times or target is reached 
import random

#myway - works for 1 player with target and numer of times they roll 
# Todo - 1. just try with more players 2. Let there be a prompt to roll everytime unless they get to 50 or roll 1
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

#otherway - includes number of players with target and can roll as many times as they say yes or until they win or say no
#There is a problem, code does not exit with n and not exiting after max score is reached
def roll(): 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 10
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)