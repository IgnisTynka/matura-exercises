def zad41(lines):
    w.write(f'Zadanie 4.1\n')
    i = 0
    for line in lines:
        if line[0] == line[len(line)-3] and line[1] == line[len(line)-2]:
            i = i + 1
    w.write(f'{i}\n')

def zad42(lines):
    w.write(f'Zadanie 4.2\n')

def zad43(lines):
    w.write(f'Zadanie 4.3\n')

def decimal(line):
    result = 0


f = open('liczby_h.txt', 'r')
w = open('wynik4.txt', 'w')

lines = f.readlines()

zad41(lines)
