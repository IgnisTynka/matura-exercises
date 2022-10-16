def isPalindrome(x):
    if x < 0:         # negative numbers are not palindromes
        return False

    if x < 10:       # single digit numbers are palindromes
        return True

    if x % 10 == 0:      # numbers ending with 0 are not palindromes
        return False

    rev = 0
    while x > rev:      # reverse the number
        rev = rev* 10 + x % 10
        x = x / 10
    print(x)
    print(rev)
    return x == rev or x == rev / 10
