import random

fact ="""If you scramble the letters in each word, but leave 
the first and last letter alone, most people can still read the text"""

# look at each word one at a time
words = fact.split()
# print(words)
# for word in words:
for i in range(len(words)):
    word = words[i]
    # print(word)
    # take the middle part of a word (excluding 1st and last letter)
    middle = word[1:-1]
    # scramble it randomly
    mid = list(middle)
    random.shuffle(mid)
    # reassemble the word
    middle = ''.join(mid)
    word = word[0] + middle + word[-1]
    words[i] = word
    # print(word)
# reassemble the entire string
print(words)
text = ' '.join(words)
print(text)

# ... means do nothing

for i in range(len(words)):
    word = words[i]
    if len(word) == 1:
        continue # continue to run the next line of code
    # print(word)
    # take the middle part of a word (excluding 1st and last letter)
    middle = word[1:-1]
    # scramble it randomly
    mid = list(middle)
    random.shuffle(mid)
    # reassemble the word
    middle = ''.join(mid)
    word = word[0] + middle + word[-1]
    words[i] = word
    # print(word)
# reassemble the entire string
print(words)
text = ' '.join(words)
print(text)