phonebook = {'Me': '123425'}

def lookup(name):
    global phonebook
    if name in phonebook:
        return phonebook[name]
    else:
        number = input('What is the phone number of '+name+'? ')
        phonebook[name] = number
        return phonebook[name]

print('Me', lookup('Me'))
print('You', lookup('You'))
