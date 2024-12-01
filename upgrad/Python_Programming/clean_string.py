# Remove numbers and special characters and reverse upper and lower strings

#import re
inp = 'cHETU123!'
inp = list(inp)

#pattern = r'[0-9]'

# Match all digits in the string and replace them with an empty string
#out = re.sub(pattern, '', inp)

#print(out)



# Another way without using regex

# Learnings
# This is how you check every element data type in list
#ls = [type(item) for item in inp]
#print(ls)
#EndLearnings

new_string = ''.join(filter(lambda item: item.isalpha(), inp))
print(new_string)

#complete it with replacing lower with upper and upper with lower
