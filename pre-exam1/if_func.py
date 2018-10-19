def how_many_days(year):
    '''
    leap year if multiple of four unless multiple of 100 and not multiple 400
    '''
# No.1
     if (year % 4) == 0:
         if (year % 400) == 0:
             return 366
         elif (year % 100) == 0:
             return 365
         else:
             return 366
     else:
         return 365


print(how_many_days(2017), 'not leap')
print(how_many_days(2016), 'leap')
print(how_many_days(2000), 'leap')
print(how_many_days(1900), 'not leap')


def how_many_days2(year):

# No.2
    mult4 = (year % 4) == 0
    mult100 =  (year % 100) == 0
    mult400 = (year % 400) == 0
    if mult4 and ((not mult100) or mult400):
    # if mult4 and not (mult100 and (not mult400)):
        return 366
    else:
        return 365

# No.3

    if mult4:
        if mult400:
            return 366
        elif mult100:
            return 365
        else:
            return 366
    else:
        return 365

# No.4
    # if (year % 400) == 0:
    #     return 366
    # elif (year % 100) == 0；
    #     return 365
    # elif (year % 4) == 0:
    #     return 366


