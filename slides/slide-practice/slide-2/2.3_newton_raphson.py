k = float(input("Number: "))
c = 1
g = k / 2.0

epsilon = 0.01

while abs(g * g - k) >= epsilon:
    g = g - ((g ** 2) - k) / (2 * g)

print(g)

# Tracing by hand
# k = 24.0
# c = 1, not used here
# g = 24.0 / 2.0 == 12.0
# 
# while 12.0 * 12.0 - 24.0 >= 0.01 | this is equal to 144.0 - 24.0 = 120.0
# 1. set g to 12.0 - ((12.0 ** 2) - 24.0) / (24.0) | equal to 12.0 - (120.0 / 24.0) = 7.0
# while loop is now 7.0 * 7.0 - 24.0 | equal to 49 - 24 = 25
# 2. set g to 7.0  - ((7.0 ** 2)  - 24.0) / (24.0) | equal to 7.0 - (49 / 24) = 4.959 or so

