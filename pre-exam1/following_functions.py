def quad(x, a, b, c):
    global count
    count = count + 1
    # print(a, x**2, '+', b, x, '+', c, '=', a * x**2 + b * x + c)
    return a * x**2 + b * x + c


def f(x):
    # print(x)
    y = quad(x, 1, -1, -1)
    return y

x = 3
print(quad(2,1,x,5)) #positional arguments
print(f(1.6))
print('count =', count)
