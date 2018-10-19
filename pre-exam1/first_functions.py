'''
def name_of_function(parameter1, parameter2, ...):
    work (something indented)
    work
    return value

'''

#The Recipe


def tripple(n):
    n2 = n*3
    return n2

# x = 4
# y = tripple(x)
# print(y)

#return provides a value that I can use

def sextuple(n):
    n2 = tripple(n)
    return n2 * 2

def compliment():
    print('You look nice.')   


def example(x, y):
    '''returns True if x is bigger than y, False if it is not'''  # what you are trying to do
    return x > y


print(example(5,3))