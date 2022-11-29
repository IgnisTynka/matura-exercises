text = input("Wpisz tekst do zaszyfrowania: ")
vector = int(input("Wpisz wielkość przesunięcia: "))

def encryption(text, vector):
    result = ""
    for letter in text:
        if letter.isupper():
            result += chr((ord(letter) + vector - 65) % 26 + 65)
        else:
            result += chr((ord(letter) + vector - 97) % 26 + 97)
    return result

entext = encryption(text, vector)
print(entext)

entext = input("Wpisz zaszyfrowany text: ")
vector = int(input("Wpisz wielkość przesunięcia: "))

def decryption(entext, vector):
    result = ""
    for letter in entext:
        if letter.isupper():
            result += chr((ord(letter) - vector - 65) % 26 + 65)
        else:
            result += chr((ord(letter) - vector - 97) % 26 + 97)
    return result

text = decryption(entext, vector)
print(text)

