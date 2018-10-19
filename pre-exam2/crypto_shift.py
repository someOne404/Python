def index_to_letter(index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet[index % 26]

def letter_to_index(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # for i in range(len(alphabet)):
    #     if alphabet[i] == letter:
    #         return i
    # return -1
    return alphabet.find(letter)

def is_letter(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # for i in range(len(alphabet)):
    #     if alphabet[i] == letter:
    #         return True
    # return False
    return letter in alphabet


def shift(text, key):
    ans = ''
    for letter in text:
        i = letter_to_index(letter) + key
        l = index_to_letter(i)
        ans += l
    return ans

print(shift("Casesar cipher", 3), "Fdhvdu flaskhu")