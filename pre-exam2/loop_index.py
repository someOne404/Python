x = [2, 3, 5, 7]
y = [2, 4, 6, 8]

z = []
for i in range(len(x)):
    xval = x[i]
    yval = y[i]
    z.append(xval + yval)
    print(z)
print(z)

#for xval in x:
    #...

# see if x's values are in order
x = [1, 3, 2, 4, 5, 11, 9]
for i in range(len(x)-1):
    here = x[i]
    next = x[i+1] # i + 1 ... means i must stop 1 before end
    if next < here:
        print(here, ' and ', next, ' are out of order!')



s = '123'
l =[1, 2, 3]
s2, l2 = s, l
for thing in '456':
    s += thing
    l.append(thing)

print(s2, l2)
# s2 is a string, which is immutable



def ispalindrome(x):
    for i in range(len(x)):
        here = x[i]
        there = x[-1 - i]
        if here != there:
            return False
        return True

# sees if x is a palindrome
x = [1, 2, 3, 2, 1]

print(ispalindrome("atoyota"))
print(ispalindrome("acar"))