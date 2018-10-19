def f(x):
    if x < 0:
        return 0
    return 1

def g(x):
    if x < 0:
        return 0
    else:
        return 1


x = 0  #goal: make f(x) and g(x) different by picking x wisely
print(f(x))
print(g(x))

#return give the value back to the function
#return stops the function




def sqrt(x):
    if x < 0:
        return 0
    return x**0.5






num = int(input('type and int: '))

if num < 0:
    message = "negative"

if num > 100:
    message = "biggish"

if num == 1110:
    message = "the best number"

print(message)


# if the input is 1110, two ifs are true, the assigned value of message is changed

''' means it can contain multiple strings, it is the third way of quoting'''

