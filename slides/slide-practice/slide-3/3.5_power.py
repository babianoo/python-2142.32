def iter_power(base, exp):
    res = base
    while exp > 1:
        res *= base
        exp -= 1
    return res

def recur_power(base, exp):
    if exp == 1:
        return base
    else:
        return base * recur_power(base, exp - 1)

print(iter_power(5, 2))
print(iter_power(3, 3))
print(iter_power(2, 4))
print("")

print(recur_power(5, 2))
print(recur_power(3, 3))
print(recur_power(2, 4))
print(recur_power(2, 1))