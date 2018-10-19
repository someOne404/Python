d = {1:'haha', '2':456, (3,4):[5,6,7], 'hi':'there', (56,78):'rou'}
print(d.items())
print(d.keys())
print(d.values())
d[3] = 'three'
print(d.items())
print(list(d.items()))
print(list(d.keys()))
print(list(d.values()))