# Slide 1.2
s = 'azcbobobegghakl'
current = s[0]
best    = ""

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current = current + s[i]
    else:
        current = s[i]
    if len(current) > len(best):
        best = current


print(best)