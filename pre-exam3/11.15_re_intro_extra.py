import re

text = """
Per the registrar, all sections of 1110 and 1111 will have their final exam at 7–10 pm on Thursday, 7 Dec 2017. Locations are given below:
Section 	Instructor 	Exam Location
1110-001 	Tychonievich 	Chemistry 402
1110-002 	Dill 	Maury 209
1110-003 	Tychonievich 	Chemistry 402
1111-001 	Dill 	Maury 209

Conflicts with that time will be resolved the preceding day (Wednesday 6 Dec) at 7 pm, location sent via email. No permission to take the exam on a different day or from off of UVA grounds will be granted without Deans office request.

You may report conflicts and request accommodations via this form.
"""

numbers = '[0-9]+-[0-9]+'
print(type(numbers), numbers)
finder = re.compile(numbers)
print(type(finder), finder)
print(finder.findall(text))
#print(numbers.find(text)) #has nothing to do with regular expression

m = finder.search(text) # .search() find the first matched occurence
print(m)

if m != None:
    print(m.start(), m.end(), m.group()) #start()--the starting index , end()--the ending index, group()--the string that matched

for m in finder.finditer(text):
    print(m.start(), m.end(), m.group())