#Slide 1.5
x = int(input("Number: "))

# Neg check
negative = False
if x < 0: 
    negative = True 
    x = abs(x)

res = 1

while (res ** 3) < x:
    res += 1

if (res ** 3) == x:
    print(f"Found {res}")
else: print(f"Couldn't find cube root for {x}")