d ={11:'eleven', 'fun':'CS'}
l = [1, 2]
d[2] = 'two'
d['three'] = 3
print(d)
print(d[2])
print(d[11])

print(d.keys())
print(d.values())
print(d.items())

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print(d.pop(11))
print(d)

a=list(d.keys())
print(a)
# can't have two keys for one value