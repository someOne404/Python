import re
# text = r'C:\Program Files\a\\this is a test.exe'
# thing = re.compile('\\\\.')
# thing = re.compile(r'\\.')
# print(text)
# print(thing.findall(text))
# for text in thing.findall(text):
#     print(text)


text = r'C:\Program Files\.this is a test.exe'

print(text)
t = re.compile(r'\\')
print(t.findall(text))
a='\.\,\q\\'
s = re.compile('\.')
print(s.findall(text))
o = '\.'
print(o)