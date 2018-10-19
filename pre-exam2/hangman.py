# jl4nq & sbm3qh & mto3hr

word = input('Enter a word or phrase: ')
lower_word = word.lower()
underscore_word = "_".join(lower_word)+'_'
underscore = underscore_word[1:-1:2]
print("The word to guess: " + underscore)

letter = input('Guess a letter: ')
guess = underscore_word.replace(letter+'_', letter+letter)
print("The word to guess: " + guess[1::2])

if '_' in guess:
    letter = input('Guess a letter: ')
    guess_1 = guess.replace(letter + '_', letter + letter)
    print('The word to guess: ' + guess_1[1::2])

    if '_' in guess_1:
        letter = input('Guess a letter: ')
        guess_2 = guess_1.replace(letter + '_', letter + letter)
        print('The word to guess: ' + guess_2[1::2])

        if '_' in guess_2:
            letter = input('Guess a letter: ')
            guess_3 = guess_2.replace(letter + '_', letter + letter)
            print('The word to guess: ' + guess_3[1::2])

            if '_' in guess_3:
                letter = input('Guess a letter: ')
                guess_4 = guess_3.replace(letter + '_', letter + letter)
                print('The word to guess: ' + guess_4[1::2])

                if '_' in guess_4:
                    letter = input('Guess a letter: ')
                    guess_5 = guess_4.replace(letter + '_', letter + letter)
                    print('The word to guess: ' + guess_5[1::2])

                    if '_' in guess_5:
                        letter = input('Guess a letter: ')
                        guess_6 = guess_5.replace(letter + '_', letter + letter)
                        print('The word to guess: ' + guess_6[1::2])

                        if '_' in guess_6:
                            letter = input('Guess a letter: ')
                            guess_7 = guess_6.replace(letter + '_', letter + letter)
                            print('The word to guess: ' + guess_7[1::2])

                            if '_' in guess_7:
                                letter = input('Guess a letter: ')
                                guess_8 = guess_7.replace(letter + '_', letter + letter)
                                print('The word to guess: ' + guess_8[1::2])

                                if '_' in guess_8:
                                    letter = input('Guess a letter: ')
                                    guess_9 = guess_8.replace(letter + '_', letter + letter)
                                    print('The word to guess: ' + guess_9[1::2])

                                    if '_' in guess_9:
                                        letter = input('Guess a letter: ')
                                        guess_10 = guess_9.replace(letter + '_', letter + letter)
                                        print('The word to guess: ' + guess_10[1::2])
