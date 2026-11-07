#Slide 1.10
passwrd = str(input("PIN: "))
guesses = 0
found   = None

for i in range(10000):
    pin      = str(i).zfill(4)
    guesses += 1

    if pin == passwrd:
        found = pin
        break

print('Cracked PIN:', found)
print('Guesses needed:', guesses)
print('A 4-digit PIN has only 10,000 combinations - too few!')