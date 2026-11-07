def recur_mult(x, b):
    if b == 1:
        return x
    else:
        return x + recur_mult(x, b - 1)

def iter_mult(x, b):
    res = 0
    while b >= 1:
        res += x
        b -= 1
    return res

print(recur_mult(5, 4))
print(iter_mult(5, 4))