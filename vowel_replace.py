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

#Find another method without 2 for loops