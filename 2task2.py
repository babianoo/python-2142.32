epsilon = 0.01
y = float(input("Number: ")) # 27
guess = y / 2.0 # 13.5
num_guesses = 0

while abs(guess ** 3 - y) >= epsilon:
    num_guesses += 1
            # 13.5 - (2460.375 - 27) / (3 * 182.25)
    guess = guess - ((guess ** 3 - y) / (3 * guess ** 2))