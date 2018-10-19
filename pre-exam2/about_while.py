i = int(input('type an integer: '))

# while i > 0:
#     print(i)
#     i -= 1


sum = 0

# infinite loop
# happens when guard condition is not modified in the loop body
while i > 0:
    sum += i
    i -= 1

print(sum)