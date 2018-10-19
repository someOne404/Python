import random
with open('add_to_me.txt', 'a') as f:
    print(random.randrange(0,1000000),file=f)
