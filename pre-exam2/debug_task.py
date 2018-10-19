# Original written by Mark Sherriff (mss2x)
# Modified and bugs introduced by Luther Tychonievich (lat7h)
# jl4nq & sbm3qh & mto3hr

marbles = 0
pick = 0

def pow2(n):
    """Computes are returns the largest power of two that is no larger than n"""
    ans = 1
    while int(ans)*2 <= int(n):
        ans = int(ans) * 2
    return ans

print("The Game of Nim\n")
while marbles <= 0:
    marbles = int(input("The number of marbles in the pile: "))
turn_choice = input("Who will start? (p or c): ")
turn = False
if turn_choice == 'p':
    turn = True

while marbles != 0:
    print("The pile has", str(marbles), "marbles in it.")
    can_take = marbles // 2
    print('Bad: ', can_take, marbles)
    if can_take == 0:
        can_take = 1
    if turn:
        take = 0
        while take > can_take or take < 1:
            take = int(input("How many marbles to you want to take (1-" + str(can_take) + ")"))
            marbles -= take
    else:
        take = 1
        target = pow2(marbles) - 1
        take = marbles - target
        if take > marbles // 2:
            take = 1
        marbles -= int(take)
        print("The computer takes", str(take), "marbles.")

    turn = not turn

if turn:
    print("The player wins!")
else:
    print("The computer wins!")
