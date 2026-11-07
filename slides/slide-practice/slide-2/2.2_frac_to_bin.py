x = float(input("Number: "))
p = 0

while ((2 ** p) * x) % 1 != 0:
    print(((2 ** p) * x) % 1)
    print(f"p: {p}") 
    p += 1

num = int(x * (2 ** p))
res = ""

while num > 0:
    res += str(num % 2)
    num //= 2

print(f"p - len: {p - len(res)}")
for i in range(p - len(res)):
    res += '0'

res = res[0:-p] + '.' + res[-p:]
print(res)