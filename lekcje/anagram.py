f = open("anagram.txt", 'r')
o = open("odpowiedzi.txt", 'w')

lines = []
lines = f.readlines()

def liczbaZnaków(lines):
    bool = True
    for line in lines:
        line = line.split()
        firstLength = len(line[0])
        for i in range(1, len(line)):
            if len(line[i]) != firstLength:
                bool = False
        if(bool):
            line = ' '.join(line)
            o.write(f'{line}\n')
        bool = True
    return

def wszystkieAnagramy(lines):
    bool = True
    for line in lines:
        line = line.split()
        firstWord = sorted(line[0])
        for i in range(1, len(line)):
            if sorted(line[i]) != firstWord:
                bool = False
        if (bool):
            line = ' '.join(line)
            o.write(f'{line}\n')
        bool = True
    return

o.write(f'Zad 4 a)\n')
liczbaZnaków(lines)
o.write(f'Zad 4 b)\n')
wszystkieAnagramy(lines)
