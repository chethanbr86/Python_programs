word = 'I Love coding in Python'

#Reversing words
#1st method:
print(word[::-1])

#2nd method:
s = ''
for i in word:
    s = i + s

print(s)

#Reversing Strings
print(word.split(' '))
print(''.join(word[::-1])) #or can use for loop like above

# Comment: only difference between 2 types is using split


