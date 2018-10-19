import re

# addition problem: one or more numbers, separated by + or - (and maybe spaces)
ex = r'''
1
123
1 + 2 +    3
1 + - + 34 + 5 + 6 + 7 + 8 - 1
1+2+3 -4-5- 6
'''
addition = re.compile(r'[0-9]+( *(\+|\-) *[0-9]+)*')
operator = re.compile(r' *([\+|\-]) *') #special function of split in re: contents of the group will be inserted bewteen the elements in the list
for m in addition.finditer(ex):
    prob = m.group()
    parts = operator.split(prob)
    print(parts)
    ans = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == '+':
            ans += int(parts[i+1])
        else:
            ans -= int(parts[i + 1])
        # print(parts[i], parts[i+1]

    print('=', ans)

# ... and also perform the addition


#boundaries
'''
^--the beginning of everything
$--the end of everything
\b
'''