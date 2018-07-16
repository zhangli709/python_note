# class A(object):
#     def foo(self,x):
#         print(self,x)
#
#     @classmethod
#     def class_foo(cls,x):
#         print(cls,x)
#
#
#     @staticmethod
#     def static_foo(x):
#         print(x)
#
# a = A()
#
# a.foo(1)
# A.class_foo(2)
# a.static_foo(3)
# import re
#
#
# def strreplace(str, old_string,new_string):
#
#     new_string = re.sub(old_string,new_string,str)
#
#
#     return new_string
#
# pstr = 'hello world!'
#
# after_replace_str = strreplace(pstr,'world','tom')
# print(after_replace_str)
# import time
#
#
# def timer(func):
#     def deco(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return deco
#
# @timer
# def test(): #8
#     time.sleep(2)
#     print("test is running!")
#     return "Returned value"
# test()

# x = 1;y=2;z='a';
# if x << 1 >2:
#     print(X)
# elif z ==97:
#     print('Z')
# else:
#     print('y')
#
# list1 = [1,2,3,4,5,6,2]
#
# list1 = list(set(list1))
# print(list1)

#
# def upper(func):
#     def deco(*args,**kwargs):
#
#         res = func()
#         res = res.capitalize()
#         return res
#     return deco
#
# @upper
# def greetings(word='hi there'):
#     return word.lower()
#
# print(greetings())

# x = 'hello world'
# x.replace('hello','hi')
# print(x)
# list1 = [' ', '     ', 'a', 'b', 'c', 'd', '      ']
#
#
# l = []
# for i in list1:
#     if not i.isspace():
#         l.append(i)
#
# print(l)


#
# list1 = [1,2,3,4,5,6,7,8,324,5,4,45645,]
# list1.reverse()
# print(list1)

# def isprime(num):
#     for i in range(2,num):
#         for j in range(2,i-1):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
#
# isprime(100)

# def sort(ndarray):
#     sort_nd = [ndarray[0],ndarray[1] if ndarray[0] < ndarray[1] else ndarray[1],ndarray[0]]
#     print(sort_nd)
#     for i in ndarray[2:]:
#         for index, j in enumerate(sort_nd):
#             if i > sort_nd[index] and i < sort_nd[index+1]:
#                 sort_nd.insert(index+1,i)
#             elif i < sort_nd[index]:
#                 sort_nd.insert(index,i)
#             else:
#                 sort_nd.append(i)
#
#     return sort_nd
#
#
# a = [1,22,3,33,5,6,7,8]
# # sort(a)
# print(a)
# print(a[2:])

# x = 4
# y = 6
#
# (x, y) = (x, y) if x > y else (y, x)
# print(x)

# 冒泡
# def bubble_sort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1] ,nums[j]
#     return nums
#
# print(bubble_sort([22,55,24,54,77,11,26,24]))

# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b,a+b
#     yield a
#
# print(fib(10))

# from datetime import datetime
# import time
#
# time.sleep(1)
# print(datetime.now())


# 水仙花
# for n in range(100,1000):
#     i = n // 100
#     j = n//10 % 10
#     k = n % 10
#     if n == i **3 + j ** 3 + k**3:
#         print(n)


# 分解因数

# print(reduce_num(22))x = int(input("是否进入循环？是：1， 否：0\n"))
# while(x):
#     n = int(input("请输入一个正整数："))
#     print ("%d = " %n , end = '')
#     while n not in [1]:
#         for index in range(2, n+1):
#             if n % index == 0:
#                 n = int(n/index)
#                 if n == 1:
#                     print("%d " %index , end = '')
#                 else:
#                     print("%d * " %index , end = '')
#                 break
#     print()
#     x = int(input("是否进入循环？是：1， 否：0\n"))
#
#

# from datetime import datetime
#
# date_= datetime.now()
#
# print('%s/%s/%s' %(date_.month,date_.day,date_.year))
# x = input('xxx')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for i in x:
#     if i.isspace():
#         space+=1
#     elif i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         letters+=1
#     else:
#         others +=1
# print(letters,space,digit,others)


#
# def ball(s,n=10):
#     if n > 0:
#         n -=1
#
#         return ball(s/2,n=n)
#     if n == 0:
#         print(s/2)
#
#
# a =ball(100)
#
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j ==0:
#             break
#     else:
#         print(i)

dict1 = {'a':1,'b':2,'c':3}
for k,v in dict1.items():
    print(k,":",v)