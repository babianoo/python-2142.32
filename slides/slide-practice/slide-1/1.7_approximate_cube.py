#Slide 1.7
epsilon   = 0.01
x         = float(input("Number: "))
negative  = False
if x < 0:
    negative = True
    x = abs(x)

increment = 0.0001
guesses   = 0

current   = 0
while current ** 3 < x - epsilon:
    current += increment
    guesses += 1

if negative:
    print(f"{guesses} guesses to find cube root for -{x} being -{current} approximately")
else:
    print(f"{guesses} guesses to find cube root for {x} being {current} approximately")