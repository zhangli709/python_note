# # import re
# #
# #
# # def main():
# #     num = input('请输入你要查询的电话号码的前三位数字：')
# #     # compare_num = re.compile(r'^"1"(0[3]|1[8])\d')
# #     if re.match(r'^13\d', num):
# #         print('是')
# #     elif re.match(r'^14(5|7)', num):
# #         print('是')
# #     elif re.match(r'15([0-3]|[5-9])', num):
# #         print('是')
# #     elif re.match(r'^17(6|7|8)', num):
# #         print('是')
# #     elif re.match(r'^18\d', num):
# #         print('是')
# #     else:
# #         print('不是')
# #
# #
# # if __name__ == '__main__':
# #     main()
# #
# #
#
#
#
import re


def main():
    patten = re.compile(r'(?<=\D)1[345789]\d{9}(?=\D)')
    # match  从头找， search 任意位置找
    sentence = '重要的事情说8130123456780次,我15584548020，父亲15108390494,邓13350490494 '
    # mylist = patten.findall(sentence)
    # print(mylist)   一下全部找出来

    for temp in patten.finditer(sentence):
        print(temp)
        print(temp.group())  # 内容
        print(temp.span())  # 哪一段    一个一个找出来用。

    # m = patten.search(sentence)
    # print(m)
    # while m:
    #     print(m.group())
    #     m = patten.search(sentence, m.span()[1])

if __name__ == '__main__':
    main()
#
#
# #  脏话过滤  re.sub
#
# import re
#
#
# def main():
#     # sentence = ''
#     # re.sub('正则表达式', '替换的内容，一般为*', sentence, flags=re.IGNORECASE)   # 最后为忽略大小写。
#
#     sentence = '傻逼，日你妈，滚，你大爷，你妈的'
#     new_sentence = re.sub(r'[傻逼日滚]|你妈的', '呵呵', sentence, flags=re.IGNORECASE)
#     print(new_sentence)
#
#
# if __name__ == '__main__':
#     main()
#
#
# #  sub.split -- 拆分。
#
# import re
#
# def main():
#     sentence = '才如此难过,相爱的把握　要如何再搜索,相拥着寂寞　难道就不寂寞,爱本是泡沫　怪我没有看破'
#     new_sentence = re.split('[ ,]', sentence)
#     print(new_sentence)
#
#
# if __name__ == '__main__':
#     main()



# re
#  split