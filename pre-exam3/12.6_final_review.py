for num in range(2):
    print(num)

for num in range(1,2):
    print(num)

def justify_string(s):
    list_words = s.split()
    length = 0
    for word in list_words:
        length += len(word)
    spaces_needed = 80 - length
    while spaces_needed > 0 :
        for i in range(len(list_words)-1):
            if spaces_needed > 0:
                list_words[i] += '.'
                spaces_needed -= 1
    return ''.join(list_words)

print(justify_string('Assume for this question that'))

print('s' == 'S')

def count_common(s1,s2):
    common_letter = []
    for letter in s1:
        if letter in s2 and letter not in common_letter:
            common_letter.append(letter)
    return len(common_letter)


