def space_remove(text):
    result = ""
    for l in text:
        if l != " ":
            result += l
    return result

def encrytion(text, key):
    n = len(key)
    if len(text) % n == 0:
        m = len(text)//n
    else:
        m = (len(text) // n) + 1
    pom = tab = [[0 for col in range(n)] for row in range(m)]
    l = 0
    for i in range(m):
        for j in range(n):
            if (l < len(text)):
                pom[i][j] = text[l]
                l += 1
            else:
                pom[i][j] = ""
    szyfr = ""
    for d in key:
        for j in range(m):
            if pom[j][int(d)] != "":
                szyfr += pom[j][int(d)]
    return szyfr

text = input("Enter text: ")
key = input("Enter key: ")

print(encrytion(space_remove(text), key))
