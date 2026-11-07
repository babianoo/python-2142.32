def factorial_recur(a):
    print(f"a: {a}")
    if a == 1:
        return a
    else:
        return a * factorial_recur(a - 1)

def factorial_iter(a):
    res = a
    while a != 1:
        a -= 1
        res *= a
    return res

print(factorial_recur(4))
print(factorial_iter(4))