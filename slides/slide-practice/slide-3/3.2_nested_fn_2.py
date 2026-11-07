def foo(x):
    def bar(y, z = 0):
        return y + x
    return bar(3, x)

def foo2(x):
    def bar2(y, z = 0):
        return y + x
    return bar2(3)

print(foo(2)) # 5
print(foo2(5)) # 8