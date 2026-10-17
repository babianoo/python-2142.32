def iterDiv(a, b):
    """Finds integer quotient using not recursion :3"""
    sub_count = 0
    while (a - b) >= 0:
        sub_count += 1
        a -= b
    return sub_count

def recurDiv(a, b):
    """Finds integer quotient using recursion"""
    if (a - b) < 0:
        return 0
    return 1 + recurDiv(a - b, b)

print(iterDiv(17, 5))
print(recurDiv(17, 5))