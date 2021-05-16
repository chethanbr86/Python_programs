# Remove numbers and special characters and reverse upper and lower strings

import re
inp = 'cHETU123'

pattern = r'[0-9]'

# Match all digits in the string and replace them with an empty string
out = re.sub(pattern, '', inp)

print(out)

#complete it with replacing lower with upper and upper with lower