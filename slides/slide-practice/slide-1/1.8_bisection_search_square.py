#Slide 1.8
# Probably should look over this one again

x       = float(input("Number: "))
if x < 0:
    exit(1)

# x = 25
# guess = 12.5

high    = x
low     = 0
guess   = (high + low) / 2.0
epsilon = 0.01
guesses = 0

# While the distance to 0 is NOT near epsilon
while abs(guess ** 2 - x) >= epsilon:
    guesses += 1

    # Chop left
    if guess ** 2 < x:
        low  = guess
    else:
        high = guess
    # Chop right

    guess = (high + low) / 2.0

print(f"{guesses} guesses for the square of {x} being {guess}")