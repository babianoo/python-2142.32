s = 'azcbobobegghakl'
res = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        res += 1
print(res)
