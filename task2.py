binary = input("Enter a binary number: ")
correct = True
number = 0

# Check
for i in range(len(binary)):
    if binary[i] != "1" and binary[i] != "0":
        correct = False

if correct is True:    
    for i in range(len(binary)):
        if binary[len(binary) - i - 1] == "1":
            number += 2 ** i
    print(f"{binary} in decimal is {number}")
else:
    print(f"{binary} is not a binary number")