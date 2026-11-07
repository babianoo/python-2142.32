#Slide 1.4
x = int(input("Number: "))
res = 1

while (res ** 3) < x:
    res += 1

if (res ** 3) == x:
    print(f"Found {res}")
else: print(f"Couldn't find cube root for {x}")