def lcmIter(a, b):
    if b > a:
        prev = b
        while b % a != 0:
            b += prev
        return b
    else:
        prev = a
        while a % b != 0:
            a += prev
        return a

def gcdRecur(a, b):
    if b == 0: return a
    return gcdRecur(b, a % b)

def lcmRecur(a, b):
    return a * b / gcdRecur(a, b)

print(gcdRecur(12, 18))
print(lcmIter(12, 18))