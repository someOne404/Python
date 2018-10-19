with open('file_1.txt', 'w') as f:
    print('Here is some', file=f)
    print('text that we can', file=f)
    print('compare with', file=f)
    print('another file.', file=f)
    print('', file=f)
    print('Even with a', file=f)
    print('blank line!', file=f)
with open('file_2.txt', 'w') as f:
    print('Here is some', file=f)
    print('text that I can', file=f)
    print('compare with', file=f)
    print('another file....', file=f)
    print('', file=f)
    print('Even with a', file=f)
    print('blank thingy!', file=f)
    print('And an extra line!', file=f)
    print('And an extra line!', file=f)

file_name_1 = input('First file: ')
file_name_2 = input('Secon file: ')
key1 = open(file_name_1)
key2 = open(file_name_2)
lst1 = []
lst2 = []
for line in key1:
    lst1.append(line.strip())
for line in key2:
    lst2.append(line.strip())

print(lst1)
print(lst2)
max_len = max(len(lst1), len(lst2))
print(len(lst1))
print(len(lst2))
print(max_len)
for row in range(max_len):
    if row >= len(lst1):
        print('Line: '+str(row))
        print('< [none]')
        print('> ' + lst2[row])
    elif row >= len(lst2):
        print('Line: '+str(row))
        print('< ' + lst1[row])
        print('> [none]')
    elif lst1[row] != lst2[row]:
        print('Line: '+str(row))
        print('< '+lst1[row])
        print('> ' + lst2[row])


    # if lst1[row] == '':
    #     print('< [none]')
    #     print('> ' + lst2[row])
    # elif lst2[row] == '':
    #     print('< ' + lst1[row])
    #     print('> [none]')
    # else:
    #     print('< '+lst1[row])
    #     print('> '+lst2[row])

