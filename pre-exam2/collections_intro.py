# tuple
x = (1, 2.3**2, 'hi', -1, -1, -1)
print(x)
print(x[2])
print(x[1:4])
print(len(x))
print(x + (8,2))
print(x * 3)

def divrem(n, d):
    i = n//d
    r = n % d
    return i, r


t = divrem(1110, 17)
print(t, len(t), t[0], t[1], t*3)
whole = t[0]
remainder = t[1]
print('1110 ÷ 7 is', whole, 'remainder', remainder)

# unpack the tuple (cannot unpack to variables fewer than the argument within tuple
w, r = divrem(1110, 17)
print('1110 ÷ 7 is', w, 'remainder', r)


# list
x = [1, 2.3**2, 'hi', -1, -1, -1]
print(x)
print(x[2])
print(x[1:4])
print(len(x))
print(x + [8,2])
print(x * 3)
print("hi" + "tter")

y = x
print('y', y)
print('x', x)
x[2] = 'Whee!'
print('x', x)
print('y', y)


x = [1, 2, 'three']
y = x[:] #entire copy
x[1] = 11
print(x[2][3])
y = [4, 5, 6]


x = [1, 2, 3]
y = 2 * x
x[2] = 11
print(y)
x[2] = 11
y = 2 * x
print(y)


# range
x = range(10)
print(x, len(x), x[0], x[-1], x[1:4])
x = range(6, 13)
print(x, len(x), x[0], x[-1], x[1:4])
print(list(x))

x = [1, 2, "hi", 5]
indices = range(len(x))
print(x)
print(list(indices))
