import urllib.request

# step 1: open the file
key = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/1110/2017-09-01-1400-demo.py')
print(key)

# step 2: read the text in the file
bytes = key.read()
# step 3: decode the text
text = bytes.decode('utf-8')
print(text.upper())