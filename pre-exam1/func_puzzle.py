def f(x):
    print('f')
    return x + 1

def g(a,b):
    return f(a) * f(b)     # 4 * 5

def h(y):
    return g(y, y+1) + f(y-1)       # 20 + f(y-1)

print(h(3))
