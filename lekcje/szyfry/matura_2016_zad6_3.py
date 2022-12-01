f = open("dane_6_3.txt", 'r')
o = open("wyniki_6_3.txt", 'w')

lines = []
lines = f.readlines()

def find_cryptogram(lines):
    for line in lines:
        word = line[0:-1].split(' ')
        vector = (ord(word[1][0])-65) - (ord(word[0][0])-65) % 26
        print(chr((ord(word[0][0]) + vector - 65) % 26 + 65))
        for i in range(len(word[0])):
            if chr((ord(word[0][i]) + vector - 65) % 26 + 65) != word[1][i]:
                o.write(f'{line}\n')
                break
        vector = 0

find_cryptogram(lines)