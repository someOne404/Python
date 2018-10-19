f = open('written.txt', 'w')
#f.write("This is a test")
#f.write("This is a another test")
print("hi", 3, [1,2,3], file=f)
print(3.14159*7, file=f)
f.close()


with open('written.txt', 'w') as f:
    print("hi", 3, [1,2,3], file=f)
    print(3.14159*7, file=f)

