# function names should be lower-case, short, and suggest action or returning


def quadratic(x, a, b, c):
    """evaluates a quaratic equation
    Evaluates a x**2 + b x + c (a quadratic polynomial in power basis)

    x: the variable in the equation
    a: coefficient of the quadratic term
    b: coefficient of the linear term
    c: constant
    """
    return (a * x**2) + (b * x) + c


print(quadratic(2, 3, 4, 5))



# double blank lines bewteen function and other things

# Every function should begin with doc strings
#    - evaluates a quadratic equation - brief summary of the function's purpose
#    - a more explicit description of the function what it's doing