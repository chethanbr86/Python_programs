my_string = 'thrusday'

#Replace vowels with x
def vow(word):	
	print(my_string)
	word_new = list(my_string)
	print(word_new)
	for index,j in enumerate(word):
		for k in 'aeiou':
			if j == k:
				word_new[index] = 'x'
				print(word_new)
	return ''.join(word_new)
			
print(vow(my_string))

#geeksforgeeks method using replace
def vowel(word, x):
	for i in 'aeiou':
		word = word.replace(i, 'x')
	return word

print('2nd method answer')
print(vowel(my_string, 'x'))

#First method without enumerate
def vower_string(my_string, x):
	#your_string = list(my_string)
	new_word = []

	for i in my_string:
		for j in 'aeiou':
			if i == j:
				new_word.append(x)
				# print(new_word)
				break
		else:
			new_word.append(i)
			# print(new_word)
	return ''.join(new_word)

print('3rd method')
print(vower_string(my_string,'x'))