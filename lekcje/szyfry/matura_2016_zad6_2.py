f = open("dane_6_2.txt", 'r')
o = open("wyniki_6_2.txt", 'w')

lines = []
lines = f.readlines()

def decrypted(lines):
    result = ""
    vector = 0
    for line in lines[0:700]:
        word = line[0:-1].split(' ')
        vector = int(word[1])
        for letter in word[0]:
            result += chr((ord(letter) - vector - 65) % 26 + 65)
        o.write(f'{result}\n')
        result = ""
        vector = 0



decrypted(lines)