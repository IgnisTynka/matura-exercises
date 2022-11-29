f = open("dane_6_1.txt", 'r')
o = open("wyniki_6_1.txt", 'w')

lines = []
lines = f.readlines()

def encrypted(lines):
    result = ""
    for line in lines:
        for i in range(len(line)-1):
            result += chr((ord(line[i]) + 107 - 65) % 26 + 65)
        o.write(f'{result}\n')
        result = ""

encrypted(lines)