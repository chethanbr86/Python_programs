from typing import Counter


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

total1 = 0
combined = name1.lower() + name2.lower()

t = combined.count('t')
r = combined.count('r')
u = combined.count('u')
e = combined.count('e')

true = t + r + u + e

l = combined.count('l')
o = combined.count('o')
v = combined.count('v')
e = combined.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))
print(love_score)

if love_score < 10 or love_score > 90:
    print(f'your love score is {love_score} like coke and mentos')
elif love_score < 50 or love_score > 40:
    print(f'your love score is {love_score} alright')
else:
    print(f'your love score is {love_score}')
    
    