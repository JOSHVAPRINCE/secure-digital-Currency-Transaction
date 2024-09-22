
def encrypt(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS = LETTERS.lower()
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            encrypted +=  LETTERS[num]
    return encrypted

dd=encrypt("arunraj",12)
print(dd)