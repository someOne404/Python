'''try:
    n = int(input('Enter an integer: '))
    while n not in range(1,101):
        print('Out of range')
        n = int(input('Enter an integer: '))
except ValueError:
    print('wrong type')
    n = int(input('Enter an integer: '))
'''
l1 = [2,3]
l2 = [99,41]
print(l1,l2)


n = input('any value: ')
print(type(n))
if type(n) != int:
    print('wrong')
print('123'[1])