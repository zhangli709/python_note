from time import time
from math import sqrt
start = time()
for num in range(2,10000):
    sum = 0
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            sum += i
            if i != num // i:
                sum += num // i
    if num == sum + 1:
        print('%d是完美数' % num)
end = time()
print((end - start), '秒')
