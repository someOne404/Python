# read a page, find the words taht follow articles (a, an, the)

import re
import urllib.request

page = urllib.request.urlopen('http://cs1110.cs.virginia.edu/project.html')

words = re.compile(' ([Aa]|[Aa]n|[Tt]he) ([A-Za-z]+)')
parens = re.compile('\(([^\)]*)\)')
after_article = []


for line in page:
    text = line.decode('utf-8').strip()
    # look for articles
    for m in words.finditer(text):
        after_article.append(m.group(2))
    for m in parens.finditer(text):
        print(m.group(1))

print(after_article)



