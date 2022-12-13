def createKey(klucz):
    nowyKlucz = ""
    for l in klucz:
        if l != " " and (l not in nowyKlucz):
            nowyKlucz += l
    return nowyKlucz

# def createAlphabets(klucz):
#     alfabet = [[],[]]
#     for i in range(len(klucz)):
#         alfabet[i].append(klucz[i])
#         for j in range(1, 27):
#             alfabet[i].append(chr((ord(klucz[i]) + j - 65) % 26 + 65))
#     print(alfabet)

klucz = input("Wpisz tekst do stworzenia alfabetu: ")
klucz = createKey(klucz).upper()
print(klucz)
