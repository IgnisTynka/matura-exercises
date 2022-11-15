# 3.32
print("3.32")
text = input("Wpisz tekst: ")
print(len(text))

# 3.33
print("\n3.33 \na)")
for i in text:
    print(i, end=" ")

print("\nb)")
for i in range(len(text)):
    print(text[(len(text) - 1) - i], end=" ")

print("\nc)")
for i in range(0, len(text), 2):    # for x in text[::2]:
    if i+1 < len(text):
        print(text[i] + text[i + 1], end=" ")
    else:
        print(text[i], end=" ")

print("\nd)")
for i in range(len(text) - 1, 0, -3):
    if i - 2 >= 0:
        print(text[i] + text[i - 1] + text[i - 2], end=" ")
    elif i - 1 >= 0:
        print(text[i] + text[i-1], end=" ")
    else:
        print(text[i])

print("\n3.36")
some_text = input("Wpisz tekst: ")
print("\na)")
for i in range(len(some_text)):
    if some_text[i] == ' ':
        print('')
    else:
        print(some_text[i], end='')

# 3.36
print("\nb)")
some_text += ' '
tem_text = ''
for i in range(len(some_text)):
    if some_text[i] == ' ':
        tem_text = str.lower(tem_text)    # jezeli chcemy ignorowac wielkosc liter
        if tem_text[0] == tem_text[len(tem_text)-1]:
            print(tem_text)
            tem_text = ''
        else:
            tem_text = ''
    else:
        tem_text += some_text[i]

print("\n3.36")
long_text = input("Wpisz tekst: ")
long_text += ' '
tem_text = ''
for i in range(len(long_text)):
    if long_text[i] == ' ':  # jezeli chcemy ignorowac wielkosc liter
        if tem_text[0] == 'p' and (len(tem_text) % 2 == 1):
            print(tem_text)
            tem_text = ''
        else:
            tem_text = ''
    else:
        tem_text += long_text[i]
