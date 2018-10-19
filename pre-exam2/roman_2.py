number = int(input('A number: '))

tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
tens_digit = (number // 10) % 10
part = tens[tens_digit]

print(part)

print(['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'][(number // 10) % 10])