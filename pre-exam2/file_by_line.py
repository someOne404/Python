key = open('file_intro.py')

line1 = key.readline() # \n  \r  \n\r \r\n
print(line1)
line2 = key.readline()
print(line2)
# once you have read it once, it won't be read twice

for text in key:
    print('text =', [text])


print([key.readline()]) # nothing left to read


key.close()
key = open('file_intro.py')


lines = key.readlines()
print(lines)