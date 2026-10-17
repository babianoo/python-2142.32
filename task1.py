s = input("Enter a string: ")
w = input("Enter a 3-letter word: ")

count = 0

for i in range(len(s)):
    split = s[i:i+3]
    if split == w:
        print(f"Found at position {i}")
        count += 1
if count > 0:
    print(f"Total: {count}")
else:
    print(f"{w} was not found")