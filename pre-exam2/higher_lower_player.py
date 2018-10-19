print("Think of a number between 1 and 100 and I'll guess it.")
number_of_guesses_allowed = int(input('How many guesses do I get? '))

upper_range = 100
lower_range = 0
number = (upper_range-lower_range)//2
comparison = input('Is the number higher, lower, or the same as ' + str(number) + '? ')

list = [number]
n = 0
for i in range(number_of_guesses_allowed-1):
    if comparison == 'higher'.lower():
        lower_range = number
        number += (upper_range - lower_range)//2
        comparison = input('Is the number higher, lower, or the same as ' + str(number) + '? ')
        list.append(number)
        n += 1
        if abs(list[-1] - list[-2]) <= 1:
            break
    elif comparison == 'lower'.lower():
        upper_range = number
        number = lower_range + (number-lower_range)//2
        comparison = input('Is the number higher, lower, or the same as ' + str(number) + '? ')
        list.append(number)
        n += 1
        if abs(list[-1] - list[-2]) <= 1:
            break
    elif comparison == 'same'.lower():
        break


if comparison == 'same':
    print('I won!') # outcome 1

elif n > 1 and abs(list[-1] - list[-2]) <= 1:
    print('Wait; how can it be both higher than ' + str(list[-2]) + ' and lower than ' + str(list[-1]) + '?') # outcome 2

else:
    ans = input('I lost; what was the answer? ')
    if int(ans) < list[-1] and comparison == 'higher'.lower():
        print("That can't be; you said it was higher than " + str(list[-1]) + "!") # outcome 3-1
    elif int(ans) > list[-1] and comparison == 'lower'.lower():
        print("That can't be; you said it was lower than " + str(list[-1]) + "!") # outcome 3-2
    else:
        print('Well played!')  # outcome 4

# jl4nq