integer = int(input('Enter an integer: '))
list = []

if integer in range(1, 4000):
    single = str(integer)[-1]
if integer in range(10, 4000):
    ten = str(integer)[-2]
if integer in range(100, 4000):
    hundred = str(integer)[-3]
if integer in range(1000, 4000):
    thousand = str(integer)[-4]

# 1-9
if integer in range(1, 4000):
    if integer in range(1, 10):
        if 1<=int(single)<=3:
            list.append(int(single)*'I')
        elif int(single)==4:
            list.append('IV')
        elif 5<=int(single)<=8:
            list.append('V'+'I'*(int(single)-5))
        elif int(single) == 9:
            list.append('IX')
    if integer in range(10, 100):
        if 0<=int(single)<=3:
            list.append(int(single)*'I')
        elif int(single)==4:
            list.append('IV')
        elif 5<=int(single)<=8:
            list.append('V'+'I'*(int(single)-5))
        elif int(single) == 9:
            list.append('IX')
        if 1<=int(ten)<=3:
            list.insert(0, int(ten)*'X')
        elif int(ten)==4:
            list.insert(0, 'XL')
        elif 5<=int(ten)<=8:
            list.insert(0, ('L'+(int(ten)-5)*'X'))
        elif int(ten)==9:
            list.insert(0, 'XC')
    if integer in range(100, 1000):
        if 0<=int(single)<=3:
            list.append(int(single)*'I')
        elif int(single)==4:
            list.append('IV')
        elif 5<=int(single)<=8:
            list.append('V'+'I'*(int(single)-5))
        elif int(single) == 9:
            list.append('IX')
        if 0<=int(ten)<=3:
            list.insert(0, int(ten)*'X')
        elif int(ten)==4:
            list.insert(0, 'XL')
        elif 5<=int(ten)<=8:
            list.insert(0, ('L'+(int(ten)-5)*'X'))
        elif int(ten)==9:
            list.insert(0, 'XC')
        if 1<=int(hundred)<=3:
            list.insert(0, int(hundred)*'C')
        elif int(hundred)==4:
            list.insert(0, 'CD')
        elif 5<=int(hundred)<=8:
            list.insert(0, ('D'+(int(hundred)-5)*'C'))
        elif int(hundred)==9:
            list.insert(0, 'CM')
    if integer in range(1000, 4000):
        if 0 <= int(single) <= 3:
            list.append(int(single) * 'I')
        elif int(single) == 4:
            list.append('IV')
        elif 5 <= int(single) <= 8:
            list.append('V' + 'I' * (int(single) - 5))
        elif int(single) == 9:
            list.append('IX')
        if 0 <= int(ten) <= 3:
            list.insert(0, int(ten) * 'X')
        elif int(ten) == 4:
            list.insert(0, 'XL')
        elif 5 <= int(ten) <= 8:
            list.insert(0, ('L' + (int(ten) - 5) * 'X'))
        elif int(ten) == 9:
            list.insert(0, 'XC')
        if 0 <= int(hundred) <= 3:
            list.insert(0, int(hundred) * 'C')
        elif int(hundred) == 4:
            list.insert(0, 'CD')
        elif 5 <= int(hundred) <= 8:
            list.insert(0, ('D' + (int(hundred) - 5) * 'C'))
        elif int(hundred) == 9:
            list.insert(0, 'CM')
        if 1<=int(thousand)<=3:
            list.insert(0, int(thousand)*'M')

    roman = ''.join(list)
    print('In roman numerals,', str(integer), 'is', roman)

else:
    print('Input must be between 1 and 3999')

#jl4nq