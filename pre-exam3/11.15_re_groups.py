import re

text = """
Per the registrar, all sections of 1110 and 1111 will have their final exam at 7–10 pm on Thursday, 7 Dec 2017. Locations are given below:
Section 	Instructor 	Exam Location
1110-001 	Tychonievich 	Chemistry 402
1110-002 	Dill 	Maury 209
1110-003 	Tychonievich 	Chemistry 402
1111-001 	Dill 	Maury 209

Conflicts with that time will be resolved the preceding day (Wednesday 6 Dec) at 7 pm, location sent via email. No permission to take the exam on a different day or from off of UVA grounds will be granted without Deans鈥� office request.

You may report conflicts and request accommodations via this form.
"""


course = re.compile('([0-9]{4,4})(-([0-9]{3,3}))')
for m in course.finditer(text):
    print(m.group(), m.group(0))
    print(m.group(1), m.group(0))
    print(m.group(2))
    print(m.groups())

print(course.findall(text))

