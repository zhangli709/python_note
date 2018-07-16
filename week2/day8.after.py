def main():
    names = ['刘备', '张飞', '曹操', '袁绍', '关羽', '赵云', '周瑜']
    scores = []
    for name in names:
        score = input('请输入%s的成绩：' % name)
        scores = scores.append(score)
    min_scores = max_scores = scores[1]
    print(scores)

    for s in scores:
        if s > max_scores:
            max_scores = s
        if s < min_scores:
            min_scores = s
    print('最高分：', max_scores)
    print('最低分：', min_scores)
    #scores = [95, 78, 62, 99, 45, 32, 80]
    # min_scores = max_scores = scores[1]
    # total = 0
    # for score in scores:
    #     if score > max_scores:
    #         max_scores = score
    #     if score < min_scores:
    #         min_scores = score
    #     total += score
    # print('最高分：', max_scores)
    # print('最低分：', min_scores)
    # print('平均分：%.2f' % (total / len(scores)))


# if __name__ == '__main__':
#     main()







# 时间和空间是不可调和的矛盾
# 软件和硬件在逻辑上是等效的
#


# 创建一个列表，自定义一个。tips:ctrl + alt + l 格式化。
# generator 生成器。tips:getsizeof ，计算内存空间
# 方括号，生成式 占很大空间。 圆括号，生成器，不管多大，都只占48的空间。
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后，元素已经准备就绪，所以需要耗费更多的内存空间


# def str_len(s):
#     return len(s)
#
#
# def main():
#     f = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
#     f2 = sorted(f, key=str_len, reverse=True)
#     print(f2)


if __name__ == '__main__':
    main()