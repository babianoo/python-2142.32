# Based on what I remember writing on yesterday's quiz

# 1. Recursive base**exp
#    Iterative base**exp
def recur(base, exp):
    # Base case would be when exp == 0
    if exp == 0:
        return 1
    return base * recur(base, exp - 1)

print(f"Recur: {recur(5, 3)}")

def iter(base, exp):
    res = 1
    while exp > 0:
        res = res * base
        exp -= 1
    return res

print(f"Iter: {iter(5, 3)}")

# They both output 625 for 5^3, why?

# 2. Number to binary string
#    We also needed to handle negative numbers
def to_binary(n):
    if n == 0: return "0"

    negative = False
    if n < 0: negative = True
    n = abs(n)

    res = ""
    while n > 0:
        last_bit = n % 2
        res += str(last_bit)
        n = n // 2

    res = res[::-1]
    if negative:
        res = "-" + res
    return res

print(to_binary(19))
print(to_binary(0))
print(to_binary(-10))

# It is still wrong...

# 3. Some task on tuples
# I forgot what it was so I just wrote whatever here
def f_tuples(t):
    len_t = len(t)

    odds = ()
    evens = ()
    odd_pos = ()
    even_pos = ()

    for i in range(len_t):
        if t[i] % 2 == 0:
            evens += (t[i],)
        else: odds += (t[i],)

        if i % 2 == 0:
            even_pos += (t[i],)
        else: odd_pos += (t[i],)

    return odds, evens, odd_pos, even_pos


tu = (1, 5, 7, -1, 8, 90, 18, 2, -509)
o, e, op, ep = f_tuples(tu)
print(o, e, op, ep)

# I guess f_tuples does something lol

# 4. There was another task, but on lists
# I forgot what, though.
def lis(l):
    len_l = len(l)

    max = l[0]
    min = l[0]
    current = l[0]
    negative_count = 0
    for i in range(len_l):
        current = l[i]
        if current > max: max = current
        if current < min: min = current
        if current < 0:   negative_count += 1

    res = [max, min, negative_count]
    return res

listo = [1, 40, 61837, -580, 1850, 6767]
res_list = lis(listo)
print(res_list)

# Why is it printing none?
