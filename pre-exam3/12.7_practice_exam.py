def middle(s):
    if len(s)%2 != 0:
        return s[len(s)//2]
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]

print(middle('power'))
print(middle('glow'))


lst = []
num = int(input('Type a number: '))
while num!= 0:
    lst.append(num)
    num = int(input('Type a number: '))
lst.append(num)
lst.sort()
print(lst)

def save_list(filename,data):
    with open(filename,'w') as f:
        for list in data:
            line = ''
            for i in list:
                line+= str(i)+','
            print(line[:-1], file=f)

save_list('temp,csv',[[2,3],[5,7,11],[13]])


def word_wrap(s):
    words = s.split()
    lines = ['']
    i = 0
    for word in words:
        if len(lines[i])+len(word) <80:
            lines[i]=lines[i]+' '+word
        else:
            i +=1
            lines.append(word)
    for line in lines:
        print(line.strip())

word_wrap('Write a function called word_wrap that takes a paragraph of text as a string and prints it to the screen such that each line is as close to 80 characters long as possible')


def most_common_names(names_list):
    max_count = 0
    max_name = ''
    for name in names_list:
        if max_count < names_list.count(name):
            max_count = names_list
            max_name = name
    return max_name



