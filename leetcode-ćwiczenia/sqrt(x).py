def mySqrtI(x):
    if x == 1 or x == 0:
        return x

    start = 0
    end = x // 2

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

def mySqrtF(x):
    if x < 2:
        return x

    start = 0
    end = x // 2

    while start <= end:
        mid = (start + end) / 2
        n = mid*mid
        if ((n == x) or abs(n - x) < 0.00001):
            return mid
        elif n < x:
            start = mid
            result = mid
        else:
            end = mid

    return result

x = int(input("Podaj x:"))
print(mySqrtI(x))

x = float(input("Podaj x:"))
print(mySqrtF(x))
