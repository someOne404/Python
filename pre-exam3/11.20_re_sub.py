import re

n = '''
Tychonievich, Luther
Luther Tychonievich
'''

name = re.compile(r'([A-Z][a-z]*), ([A-Z][a-z]*)')
for m in name.finditer(n):
    print(m.group(), m.groups())
    fix = m.group(2) + ' ' +m.group(1)
    print(fix)


f = name.sub(r'\2 \1 (orginial: \1, \2)', n) # in n, find name, and replace it with the expression (group1 groups2)

ana = re.compile('ana')
banana = "bananananana"
fixed = ana.sub('a', banana)
print(fixed)
fixed = ana.sub('a', fixed)
print(fixed)
fixed = ana.sub('a', fixed)
print(fixed)