klucz = input("Wpisz tekst do stworzenia alfabetu (wielkie litery): ")
text = input("Wpisz tekst do zaszyfrowania (wielkie litery): ")
klucz = klucz.upper()
text = text.upper()

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

print(encryption(text, klucz))