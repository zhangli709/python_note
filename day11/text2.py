def record(fn):
    def wrapper(*args, **kwargs):
        print('准备执行%s函数之前...' % fn.__name__)
        print(args)
        print(kwargs)
        # 此行代码在执行被装饰的函数
        # 在这行代码的前后我们可以附加其他的代码
        # 这些代码可以让我们在执行函数时做一些额外的工作
        val = fn(*args, **kwargs)
        print('%s函数执行完成' % fn.__name__)
        return val
    return wrapper


# 通过修饰器修饰f函数，让f函数在执行时，可以进行更多的操作
@record  # 合二为一
def f(n):
    if n == 0 or n == 1:
        return 1
    return n * f(n-1)


if __name__ == '__main__':

    print(f(5))

# 装饰器 让我们看出函数里面到底发生了什么。