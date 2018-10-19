def rev1(x):
    """return a new list that is x, but backwards"""
    ans = []
    for element in x:
        # put the lement at the front of ans
        ans.insert(0, element)
    return ans

x = [1, 3, 2, 8]
print(x, rev1(x))


def rev2(x):
    """reverse a list in place"""
    for i in range(len(x)//2):
        # swap current and mirrored element
        y = x[i]
        x[i] =x[-1-i]
        x[-1-i] = y
    # # swap the nex-to-first and next-to-last
    # y = x[1]
    # x[1] =x[-2]
    # x[-2] = y
    # ...

x = [1, 3, 4, 7, 9]
rev2(x)
print(x)
