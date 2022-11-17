text = input('Wpisz teskt: ')
text = text.replace(' ', '')
if text == text[::-1]:
    print('Jest palindromem')
else:
    print('Nie jest palindromem')

