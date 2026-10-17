import random
import time

now = time.time()
random.seed(now)

listLength = 40
def listWork():
    nums = []
    nums_div_3 = []
    index_div_5 = []
    for i in range(listLength):
        rand_n = random.randint(1, 50)
        nums.append(rand_n)
        if rand_n % 3 == 0:
            nums_div_3.append(rand_n)
        if i % 5 == 0:
            index_div_5.append(rand_n)
        
    return nums, nums_div_3, index_div_5

l, l_div_3, i_div_5 = listWork()

print(l)
print(len(l))
print(l_div_3)
print(len(l_div_3))
print(i_div_5)
print(len(i_div_5))