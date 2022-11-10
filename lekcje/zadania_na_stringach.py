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
    print(text[(len(text)-1)-i], end=" ")

# print("\nc)")
# for i in range(len(text), ):
#     if i+1 < len(text):
#         print(text[i], text[i+1], end=" ")
#     else:
#         print(text[i], end=" ")

