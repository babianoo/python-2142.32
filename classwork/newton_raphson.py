epsilon = 0.01
y = 24.0
guess = y / 2.0
num_guesses = 0

while abs(guess * guess - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))

print('num_guesses = ' + str(num_guesses))
print('square root of ' + str(y) + ' is about ' + str(guess))
