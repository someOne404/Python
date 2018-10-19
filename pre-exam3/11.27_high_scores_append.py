scores = []
with open('scores.csv', 'r') as f:
    for line in f:
        n, s = line.strip().split(',')
        if int(s) > 0:
            scores.append([int(s), n])
scores.sort()
scores.reverse()
for pair in scores:
    s, n = pair
    print(n, 'got', s)

name = input('Who are you? ')
score = input('What was your score? ')

with open('scores.csv', 'a') as f:
    print(name+','+score, file=f)


# reading can't create file, writing can
