# print('starting')
try:
    # print('one')
    n = int(input('Type a number: '))
    # print('two')
    n2= 1 / n
    print('Inverse:', n2)
except ZeroDivisionError:  #When the previous step has error
    print('Whoops!')
except ValueError:
    print("That wasn't a number!")
except:
    print('Something else went wrong')

print('This happens')

