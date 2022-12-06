def createAlphabet(klucz):
    alfabet = []
    for l in klucz:
        if l not in alfabet:
            alfabet.append(l)
    for c in range(65, 91):
        if chr(c) not in alfabet:
            alfabet.append(chr(c))
    return alfabet
def encryption(text, klucz):
    alfabetSzyfrowy = createAlphabet(klucz)
    result = ""
    for l in text:
        result += alfabetSzyfrowy[ord(l)-65]
    return result
def decryption(text, klucz):
    alfabetSzyfrowy = createAlphabet(klucz)
    result = ""
    for l in text:
        result += chr(alfabetSzyfrowy.index(l)+65)
    return result

klucz = input("Wpisz tekst do stworzenia alfabetu: ")
text = input("Wpisz tekst do zaszyfrowania: ")
klucz = klucz.upper()
text = text.upper()

entext = encryption(text, klucz)
print(entext)

entext = input("Wpisz tekst do zaszyfrowania: ")
entext = entext.upper()

detext = decryption(entext, klucz)
print(detext)
