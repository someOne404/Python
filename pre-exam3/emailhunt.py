# jl4nq
import re
import urllib.request

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.html')

text = []
for line in stream:
    decoded = line.decode('UTF-8').strip()
    address = '([0-9a-zA-Z.-]+@[0-9a-zA-Z-.]*)'
    finder = re.compile(address)
    for m in finder.finditer(decoded):
        print(m.group())


