def mean(a, b, c):
    x = (a + b +c) / 3
    return x

def median(a, b, c):
    if (max(a, b, c) == b and min(a, b, c) == c) or (max(a, b, c) == c and min(a, b, c) == b):
        return a
    elif (max(a, b, c) == a and min(a, b, c) == c) or (max(a, b, c) == c and min(a, b, c) == a):
        return b
    elif (max(a, b, c) == a and min(a, b, c) == b) or (max(a, b, c) == b and min(a, b, c) == a):
        return c


def rms(a, b, c):
    y = (mean(a**2, b**2, c**2))**(1/2)
    return y

def middle_average(a, b, c):
    z = median(mean(a, b, c), median(a, b, c), rms(a, b, c))
    return z

# Burgard Lu (jl4nq)