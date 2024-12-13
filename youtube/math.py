import random
import time

operators = ['+','-','*']#,'//','%']
total_problems = 10

def problem():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operator = random.choice(operators)
    expr = str(num1) + ' ' + operator + ' ' + str(num2)
    answer = eval(expr)
    return expr, answer

score = 0
start_time = time.time()

for i in range(total_problems):
    expr, answer = problem()

    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            score += 1
            print(f'Score after {i+1} questions: {score} and ans is: {answer}')
            break 
        score -= 1

end_timme = time.time()
total_time = end_timme - start_time
print(f'total time: {round(total_time,2)} seconds')
print(f'total score: {score}')