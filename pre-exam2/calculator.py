def binop(string_for_calculation):
    '''calculates strings representing mathematical expressions

    :param a single string parameter consisting of two positive integers and a single operator between them
    :return:  the int or float value of the calculation
    '''
    string_for_calculation = string_for_calculation.strip()

    if '+' in string_for_calculation:
        first_number = int(string_for_calculation[:string_for_calculation.find('+')])
        second_number = int(string_for_calculation[string_for_calculation.find('+')+1:])
        return first_number + second_number
    elif '-' in string_for_calculation:
        first_number = int(string_for_calculation[:string_for_calculation.find('-')])
        second_number = int(string_for_calculation[string_for_calculation.find('-') + 1:])
        return first_number - second_number
    elif '*' in string_for_calculation:
        first_number = int(string_for_calculation[:string_for_calculation.find('*')])
        second_number = int(string_for_calculation[string_for_calculation.find('*')+1:])
        return first_number * second_number
    elif '/' in string_for_calculation:
        first_number = int(string_for_calculation[:string_for_calculation.find('/')])
        second_number = int(string_for_calculation[string_for_calculation.find('/')+1:])
        return first_number / second_number

# Burgard Lu (jl4nq)
