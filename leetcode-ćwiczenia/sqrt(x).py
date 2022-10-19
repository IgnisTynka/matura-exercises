def mySqrt(x):
    if x == 1 or x == 0:
        return x

    start = 0
    end = x // 2

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == x:
            return mid
        elif mid * mid <= x:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result
