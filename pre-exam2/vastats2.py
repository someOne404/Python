stream = open('vastats.csv') # no decode needed
header = stream.readline()
header = header.strip().split(',')
#print(header)


name_i = header.index('Name')
under_5_i = header.index('Under 5')
under_9_i = header.index('5 to 9')
#print(name_i, under_5_i, under_9_i)


kids_county = 0
kids_other = 0
num_county = 0
num_other = 0

for line in stream:
    row = line.strip().split(',')
    name = row[name_i]
    kids = int(row[under_5_i]) + int(row[under_9_i])
    if (name == 'Virginia') or ('Congressional District' in name):
        ... # means do nothing
    elif 'County' in name:
        kids_county += kids
        num_county += 1
    else:
        kids_other += kids
        num_other += 1

print(kids_county/num_county, kids_other/num_other)

