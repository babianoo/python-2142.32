x = int(input("Number: "))

res = ""

while x > 0:
    last_bit = x % 2
    print(f"Last bit: {last_bit}")
    res += str(last_bit)
    x = x // 2

res = res[::-1]
if len(res) > 8: exit(1)
res = res.zfill(8)

print(res)