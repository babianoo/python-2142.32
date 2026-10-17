tup = (1, 2, 3, 4, 5, 6)

def split_tuple(t):
    evens = ()
    odds  = ()
    for i in range(len(t)):
        if i % 2 == 0:
            evens += (t[i],)
        else:
            odds  += (t[i],)
    return evens, odds

evens, odds = split_tuple(tup)
print(evens)
print(odds)