text = input("Wpisz tekst: ")
pattern = input("Wpisz wzorzec: ")

if pattern.find(text):
    indexes = []
    match = True
    for i in range(len(text)):
        if text[i] == pattern[0]:
            for j in range(len(pattern)):
                if i+j >= len(text):
                    match = False
                elif text[i+j] != pattern[j]:
                    match = False
            if match:
                indexes.append(i)
            match = True
    if indexes == []:
        print("Nie znaleziono")
    else:
        for index in indexes:
            print(index, end=", ")
else:
    print("Nie znaleziono")