def foo(x, y = 5):
    def bar(z):
        return z + 1
    return bar(y * 2)

print(foo(3)) # 11
print(foo(3, 0)) # 1