"""
does:
c = 'h'
print(c)
c = 'i'
print(c)
c = ' '
print(c)
...
c = 'r'
c = 'e'
print(c)
"""

for c in 'hi there': # (1) repeat once for each element
                     # (2) assign elements (not indices) to the variable c
    print(c)

print('we still have', c)

# c is completely arbitrary

s = 'computer'
for c in s:
    print(c, s)

for c in s:
    print(s)
    s += c # it prints before s changes to computer
print('end', s)

x = [1, "two", 3.0]
thing = 123
for thing in x:
    print(thing * 2)
# thing = 1
# thing = 1*2 = 2
# thing = 'two'
# thing = 'twotwo'
# thing = 3.0
# thing = 6.0
