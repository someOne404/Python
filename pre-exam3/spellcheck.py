import urllib.request

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
list = stream.read().decode('utf-8').strip().split('\n')


print('Type text; enter a blank line to end.')
switch = True
while switch:
    entered = input()
    new_words = entered.split()
    if entered != '':
        another_list = []
        for word in new_words:
            word = word.strip()
            word = word.strip("!?',()." + '"')
            another_list.append(word)

        for word in another_list:
            if (word not in list) and (word.lower() not in list):
                print('  MISSPELLED: ' + word)

    elif entered == '':
        switch = False


# jl4nq