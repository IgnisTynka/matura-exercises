def create_alphabet(key):
    alphabet = []
    for l in key:
        if l != " " and (l not in alphabet):
            alphabet.append(l)
    for c in range(65, 91):
        if chr(c) not in alphabet:
            alphabet.append(chr(c))
    return alphabet
def encryption(text, key):
    cipher_alphabet = create_alphabet(key)
    result = ""
    for l in text:
        result += cipher_alphabet[ord(l)-65]
    return result
def decryption(text, key):
    cipher_alphabet = create_alphabet(key)
    result = ""
    for l in text:
        result += chr(cipher_alphabet.index(l)+65)
    return result

key = input("Wpisz tekst do stworzenia alfabetu: ")
text = input("Wpisz tekst do zaszyfrowania: ")
key = key.upper()
text = text.upper()

entext = encryption(text, key)
print(entext)

entext = input("Wpisz tekst do zaszyfrowania: ")
entext = entext.upper()

detext = decryption(entext, key)
print(detext)
