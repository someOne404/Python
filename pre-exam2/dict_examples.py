l = [1, 'hi']
x = 'yes'
d = {1:'one', 'hi': [1,2], x+'x':x*2}

print(l,d)

print(l[0], d['yesx'])
l[0] = 123
d['hi'] = 'hello'
print(l,d)

l.append('whee!')
d[1110] = 'the best!'


# .keys(), .values(), items(), pop(...)

pb = {'Zhao': '555-1234', 'Dill': '555-5678'}
print(pb)
pb['The dean'] = '555-5555'
print('keys: ', pb.keys())
print('values', pb.values())
# values can be the same, but no the keys
print('items:', pb.items())

for number in pb.values():
    print('Calling: ', number, '...')

for name in pb.keys():
    number = pb[name]
    print('Calling: ', name, 'at', number, '...')
    pb[name] = '(434)' + number

for items in pb.items():
    name, number = items
    print('Calling: ', name, 'at', number, '...')

for name, number in pb.items():
    print('Calling: ', name, 'at', number, '...')


# .pop(key) -> 1. give me d[key] and 2. remove that key and value from d
print(pb)
pb.pop('Zhao')
print(pb)
number = pb.pop('Dill')
print(pb)
print(number)

l = [1,2,3]
print(1 in l)
print(4 in l)

print('-----------------------')
print('The dean' in pb.keys(), 'true')
print('The dean' in pb.values(), 'false')
print('The dean' in pb) # pb means pb.keys
print('-----------------------')
print('(434)555-5555' in pb.keys(), 'false')
print('(434)555-5555' in pb.values(), 'true')
print('(434)555-5555' in pb)

