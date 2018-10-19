text = '''name, value
three, 3
pi, 3.1415926535828
huandred, 100
'''
lines = text.strip().split('\n')
header = lines[0]
data = lines[1:]
print(header)
print(data)
total = 0
for line in data:
    row = line.split(',')
    number = float(row[1])
    total += number
print(total)
