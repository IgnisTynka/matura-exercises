def tab_size(text):
    d = len(text)
    n = 1
    while (n * n < d):
        n += 1
    return n

#bez usuwania spacji
def encrytion_v1(text):
    n = tab_size(text)
    pom = tab = [[0 for col in range(n)] for row in range(n)]
    l = 0
    for i in range(n):
        for j in range(n):
            if (l >= len(text) or text[l] == " "):
                pom[i][j] = "_"
                l += 1
            else:
                pom[i][j] = text[l]
                l += 1
    szyfr = ""
    for i in range(n):
        for j in range(n):
            szyfr += pom[j][i]
    return szyfr

#z usuwaniem spacji
def space_remove(text):
    result = ""
    for l in text:
        if l != " ":
            result += l
    return result
def encrytion_v2(text):
    n = tab_size(text)
    pom = tab = [[0 for col in range(n)] for row in range(n)]
    l = 0
    for i in range(n):
        for j in range(n):
            if (l < len(text)):
                pom[i][j] = text[l]
                l += 1
            else:
                pom[i][j] = "_"
    szyfr = ""
    for i in range(n):
        for j in range(n):
            if pom[j][i] != "_":
                szyfr += pom[j][i]
    return szyfr

#ALGORYTM PRZESTAWIENIOWY Z TABLICA O WYMIARACH  NxN
text = 'ALGORYTMY PRZESTAWIENIOWE'

print(encrytion_v1(text))
print(encrytion_v2(space_remove(text)))