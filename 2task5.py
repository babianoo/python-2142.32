def applyNew(L, f):
    new_list = []
    for i in range(len(L)):
        new_list.append(f(L[i]))
    return new_list

def square(x):
    return x ** 2

def applyFuns(L, x):
    for i in range(len(L)):
        print(L[i](x))

print(applyNew([1, 5, -10, -28, 90], square))
print(square(-5))
print(applyFuns([abs, round, square], -5))