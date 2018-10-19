weather = input('What\'s the "weather" like? ')
# \n  means start a new line


# weather = 'rainy' <- change weather to be 'rainy'
# weather == 'rainy' <- check to see if the weather is 'rainy'

if 'rain' in weather.lower():  # returns a new string that lowercase the input and test, but doesn't change the variable
    print('Bring an umbrella because the weather is', weather)

if 'cold' in weather.lower(): # may do this
    print('Wear mittens')
elif 'warm' in weather.lower(): # if we didn't do the last one, may do this
    print('Enjoy the warmth')
elif 'hot' in weather.lower(): # if we didn't do the last one, may do this
    print('Ugh, I hate heat')
elif 'cool' in weather.lower():
    print('Coooool!')
else:  # if we have not done any of them, do this
    print(' Imeant the temperature...')

# only check one and only one of them if it is true, if the input satisfies the first if statement, then it will not even look at other statements.
# the first if statement has the priority

print('Have a nice day!')

# >= means compare what you type based on the alphabetical order, if the typed word has a later alphabetical order, it will execute the order