#Slide 1.6
x   = int(input("Number: "))

for i in range(0, x):
    if (i ** 3) == x:
        print(f"Found {i} for {x}")
        exit(0)

print(f"Couldn't find for {x}")