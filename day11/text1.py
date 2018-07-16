
# 关键字参数-->字典 --根据参数名来决定如何执行，* 后的必须给名字
# 可变参数-->元组、不用给名字
# 命名关键字参数


# def foo(a, b, c,*, name, age): #  *后的关键字参数，必须给出参数名-命名关键字参数
#     print(a+b+c)
#     print(name, ':', age)
#
# def say_hello(**kwargs):
#     print(kwargs)
#     for key in kwargs:
#         print(key,'-->',kwargs)
#     if 'name' in kwargs:
#         print('你好，%s' % kwargs['name'])
#     elif 'age' in kwargs:
#         age = kwargs['age']
#         if age <= 16:
#             print('你还是个孩子')
#         else:
#             print('你是个成年人')
#     else:
#         print('请提供个人信息')
#
#
# def main():
#     say_hello(name='张立', age=14)
#     param = {'name': '王大锤', 'age': 16, 'tel': '1234567898'}
#     # 如果希望将一个字典当作可变参数
#     say_hello(**param)
#     mylist= [1,3,5,6,7]
#     # list  传入方法：(*列表名)
#     newlist = sorted(mylist, reverse = True)
#     print(newlist)
#     foo(1,2,3,name='zl',age=23)
#     foo(a=1,b=2,c=3, name='zl', age=23)
#     foo(1, 2, c=3,name='zl', age=24)
#
#
# if __name__ == '__main__':
#     main()




# 高阶函数
# 通过向函数中传入函数，可以写出更通用的代码
# calc函数中的第二个参数是另一个函数，他代表了一个二元运算
# 所以calc函数变得通用性更强，可以由传入的第二个参数来决定到底做什么
# 高内聚， 低耦合 high cohesion low coupling

# 1. 函数作为别个函数的参数传入
def calc(my_list, op):
    total = my_list[0]
    for index in range(1, len(my_list)):
        total = op(total, my_list[index])
    return total

#
# def my_mul(my_list):
#     total = 1
#     for val in my_list:
#         total *= val
#     return total


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def main():
    my_list = [1, 3, 5, 7, 9]
    print(calc(my_list, add))
    print(calc(my_list, mul))


if __name__ == '__main__':
    main()

# 2. 函数里面返回一个函数