# In an encrypted messaged, input is jumbled such that, first charcter of first workd is followed by first character of second word and so on.
# You have to break encrypttion and if the size or len of 2 string are not equal, then smalled word should be appended with #

inp = 'bmaunmdbraai'

city = []
state = []

for i in range(len(inp)):
    if i % 2:
        state.append(inp[i])
    else:
        city.append(inp[i])

if len(city) < len(state):
    city.append('#')
elif len(city) > len(state):
    state.append('#')
        

print(''.join(state)+','+''.join(city))