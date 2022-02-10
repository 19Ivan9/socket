def caesar_encrypt(key: int):
    alph = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    txt = 'cat'
    encrypted_msg = ''

    for letter in txt:
        position = alph.find(letter)
        new_let = position + key
        if letter in alph:
            encrypted_msg = encrypted_msg + alph[new_let]
            continue
        encrypted_msg = encrypted_msg + letter

    return encrypted_msg

