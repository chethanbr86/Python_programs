word = input()
word = word.lower()

palin = word[::-1]
if palin == word:
    print('Palindrome')
else:
    print('Not a Palindrome')