num = int(input('A number: '))

ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
thousands = ['', 'M', 'MM', 'MMM']

ones_digit = num % 10
tens_digit = (num // 10) % 10
hundred_digit = (num // 100) % 10
thousands_digit = (num // 1000) % 10
roman = thousands[thousands_digit] + hundreds[hundred_digit] + tens[tens_digit] + ones[ones_digit]
