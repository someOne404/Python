x = [1, 2, 3, 5, 1, 3, 4, 1, 4, 6, 8, 9, 1]

# sum the elements of the list
total = 0
for e in x:
    total += e
print(total / len(x))

# count the values below 4
howmany = 0
for e in x:
    if e < 4:
        howmany += 1
print(howmany, 'of the values in', x, 'were small')

# list of the small values in x
smallones = []
for e in x:
    if e < 4:
        # add_e_to_smallones
        smallones.append(e)
print(smallones)

# make a string with all elements of a list separated by space
line = ''
for e in x:
    line = line + str(e*17) + ' '
print(line)

# find the sum of the squares of the elements of x
total = 0
for e in x:
    total += e**(1/2)
print(total)