import re

# 正则表达式

def foo(mo):
    val = int(mo.group())
    return str(val**2)


def main():
    sentence = '重要的事情说1次，我的电话5，她3，他4的号码'

    m = re.sub(r'\d+', foo, sentence)
    print(m)




if __name__ == '__main__':
    main()

