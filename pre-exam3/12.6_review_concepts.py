'''
Collection types (str, list, tuple, range)
The basics of the dict datatype
Reading files and web sites
Reading tabular data (such as CSV)
'''

import random
list = [1,416,614,'asgj']
random.shuffle(list)
print(list)

#str
s1 = 'I have a pen, I have an apple'
print(s1.find('p'))

#list
l1 = [23,31,'09',123]
l1.insert(2,'31')
print(l1)
l1.remove('31')
print(l1)
print(l1.pop(2))
print(l1)
l1.reverse()
print(l1)
print(l1.index(31))
l1.sort()
print(l1)

for i in range(0,6,2):
    print(i)

#dict
d ={11:'eleven', 'fun':'CS'}
l = [1, 2]
d[2] = 'two'
d['three'] = 3
print(d)
print(d[2])
print(d[11])

print(d.keys())
print(d.values())
print(d.items())

print(d.pop(11))
print(d)

print('w=',7)

print(14.0+5)

x = {1:2, 3:4}
print(len(x))

def helper2(y,x):
    return x/y,y/x
def helper(y,x):
    return helper2(x,y)
x = 10
y =2
x,y = helper(x,y)
print(x,y)

def helper(x,y):
    x[0]=2
    y="2"
x=[1]
y="1"
helper(x,y)
print(x,y)