#codeium way
# with open('story.txt', 'r') as f:
#     story = f.read()

# for i, word in enumerate(story.split()):
#     if word == 'ADJECTIVE':
#         story = story.replace(word, input('Enter an adjective: '))
#     elif word == 'NOUN':
#         story = story.replace(word, input('Enter a noun: '))
#     elif word == 'VERB':
#         story = story.replace(word, input('Enter a verb: '))
#     elif word == 'ADVERB':
#         story = story.replace(word, input('Enter an adverb: '))
# print(story)

#youtube way
with open('youtube/story_madlib.txt', 'r') as f:
    story = f.read()

words = set() #to avoid duplicates if this was a list
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        # words.append(story[start_of_word+1:i])
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1
print(words)

answers = {}
for word in words:
    ans = input(f'Enter a {word}: ')
    answers[word] = ans
print(answers)

for word in words:
    story = story.replace(word, answers[word])
print(story)