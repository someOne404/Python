# top-down
# - know something has to repeat
# - decide what gets repeated and how often
# - turn that into code


def factorial(n):
    """compute the factorial of a number"""
    number = 1
    answer = 1
    # for every number bewteen 1 and n,
    #   multiply

    while number <= n:
        answer *= number
        number += 1

    return answer

print(factorial(6))



# bottom-up
# - write the code to do the first thing
# - write the code to do the second thing
# - write the code to do the third thing
# ...
# - notice I am repeating myself (almost)
# - one copy of the repeated stuff
#   - inside a loop
#   - make a condition, and ensure it changes to avoid infinite loop
#   - replace the thing that changes with a variable
#   -

def factors(n):
    """prints all of the factors of n"""

    thing_that_changes = 1
    while thing_that_changes <= n:
        if n % thing_that_changes == 0:
            print(thing_that_changes)
        thing_that_changes += 1

    # if n % 2 == 0:
    #     print(2)
    # if n % 3 == 0:
    #     print(3)
    # if n % 4 == 0:
    #     print(4)
    # ...
    # if n % n == 0:
    #     print(n)

factors(104)
