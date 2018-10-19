import urllib.request


key = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/vastats.csv')
text = key.read().decode('utf-8')
print(text)
lines = text.split('\n')
print(lines[:2])
line = lines[5]
print(line)
row =line.split(',')
print(row)
population = row[2]
print(population)


s = 'adjgalsdkjgklhjw'
a = s.split(';')
print(a)