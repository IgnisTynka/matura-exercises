# 3.32
print("3.32")
text = input("Wpisz tekst: ")
print(len(text))

#3.33
print("3.33 \na)")
for i in range(len(text)):
    print(text[i], end=" ")

print("\nb)")
for i in range(len(text)):
    print(text[(len(text) - 1) - i], end=" ")

print("\nc)")
for i in range(0, len(text), 2):
    if i+1 < len(text):
        print(text[i], end="")
        print(text[i + 1], end=" ")
    else:
        print(text[i], end=" ")

print("\nd)")
for i in range(len(text) - 1, 0, -3):
    if i - 2 >= 0:
        print(text[i], end="")
        print(text[i - 1], end="")
        print(text[i - 2], end="  ")
    elif i - 1 >= 0:
        print(text[i], end="")
        print(text[i-1])
    else:
        print(text[i])


