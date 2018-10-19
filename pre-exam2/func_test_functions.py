def test_pow(f):
    '''
    given a function, see if it is the pow function
    checks if f(x,y) == x**y

    :param f: a function to test
    :return: the ratio of tests passed
    '''

    passed = 0
    failed = 0

    if f(1,1) != 1:
        print('failed to compute 1**1 correctly')
        failed += 1
    else:
        passed += 1

    if f(2,5) != 32:
        print('failed to compute 2**5 correctly')
        failed += 1
    else:
        passed += 1

    return passed / (passed + failed)



# same as
# if
# elif:
# else:
#    return

def pow2(x,y):
    return x

print(test_pow(pow2))
print(test_pow(pow))


