import random
num = random.randrange(1, 101)

self_pick_answer = int(input('What should the answer be? '))
number_of_guesses = int(input('How many guesses? '))
guess = int(input('Guess a number: '))

number_of_guesses_used = 1
while self_pick_answer != guess and number_of_guesses_used < number_of_guesses:
    if self_pick_answer != -1:
        if self_pick_answer > guess:
            print('The number is higher than that.')
            guess = int(input('Guess a number: '))
        elif self_pick_answer < guess:
            print('The number is lower than that.')
            guess = int(input('Guess a number: '))
    elif self_pick_answer == -1:
        if num > guess:
            print('The number is higher than that.')
            guess = int(input('Guess a number: '))
        elif num < guess:
            print('The number is lower than that.')
            guess = int(input('Guess a number: '))
    number_of_guesses_used += 1

if self_pick_answer != -1:
    if self_pick_answer == guess:
        print('You win!')
    elif self_pick_answer != guess:
        print('You lose; the number was', str(self_pick_answer)+'.')

if self_pick_answer == -1:
    if num == guess:
        print('You win!')
    elif num != guess:
        print('You lose; the number was', str(num)+'.')


# jl4nq