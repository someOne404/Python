import urllib.request

# open, read, decode
stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/vastats.csv')
# header = first line
header = stream.readline().decode('utf-8')
header = header.strip().split(',')
print(header)

renters = 'Renter-occupied Housing'
homes = 'Occupied Housing Units'

rent_index = header.index(renters)
home_index = header.index(homes)
print(rent_index, home_index)

# ratios=[]
smallest = 1.0
where = 'nowhere'
# lines, columns, correct type
for line in stream:
    text_line = line.decode('utf-8')
    no_newline = text_line.strip()
    row = no_newline.split(',')
    houses = int(row[home_index])
    renter = int(row[rent_index])
    ratio = renter / houses
    if ratio < smallest:
        smallest = ratio
        where = row[1]
    # ratios.append(ratio)
    print(houses, renter, ratio)
print(smallest, where)

# decode means changing from bytes to texts


s = '12,34,567'
l1 = list(s)
l2 = s.split(',')
i = l2.index('34')


