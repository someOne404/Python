# mto3hr & sbm3qh & jl4nq

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def index_to_letter(index):
    return alphabet[index]


def letter_to_index(letter):
    return alphabet.index(letter)


def is_letter(letter):
    if letter in alphabet:
        return True
    else:
        return False


def interleave(plain):
    first_half = plain[:len(plain)//2+1]
    second_half = plain[len(plain)//2+1:]
    combined = []
    for i in range(len(plain)//2-1):
        a = first_half[i]
        b = second_half[i]
        combined.append(a + b)
    if len(plain) % 2 == 0:
        combined += plain[len(plain)//2]
    plain_text = ''.join(combined)
    return plain_text
print(interleave('ABCDEF'))

