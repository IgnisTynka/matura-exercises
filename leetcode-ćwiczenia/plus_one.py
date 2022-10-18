def plusOne(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
    number += 1
    number = str(number)
    digit =[]
    for i in range(len(number)):
        digit.append(int(number[i]))
    return digit

