import math
for num in range(100, 1000):
    gw = num % 10
    sw = num // 10 % 10
    bw = num // 100
    if num == pow(gw, 3) + pow(sw, 3) + pow(bw, 3):
        print('%d是水仙花数!' % num)