def check(positive_integer):
    if len(str(positive_integer)) % 2 == 0:
        every_other_digit_integer = str(positive_integer)[1::2]
        remaining_integer = str(positive_integer)[0::2]
    elif len(str(positive_integer)) % 2 != 0:
        every_other_digit_integer = str(positive_integer)[0::2]
        remaining_integer = str(positive_integer)[1::2]

    sum1 = 0
    sum2 = 0
    doubled_list = []

    for i in range(len(every_other_digit_integer)):
        sum1 += int(every_other_digit_integer[i])
    for i in range(len(remaining_integer)):
        doubled_list.append(str(int(remaining_integer[i]) * 2))
    doubled_list = ''.join(doubled_list)
    new_doubled_list = list(doubled_list)
    for i in range(len(new_doubled_list)):
        sum2 += int(new_doubled_list[i])  # how to make list into string? The intention is to add every single digit together

    total_sum = sum1 + sum2
    if total_sum % 10 == 0:
        return True
    else:
        return False

#jl4nq