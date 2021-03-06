word = input()
word_lower = word.lower()

palin = word[::-1]
if palin == word_lower:
    print('Palindrome')
else:
    print('Not a Palindrome')
