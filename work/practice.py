from random import randint

go_on = False
num1 = int(randint(1,6))
num2 = int(randint(1,6))
tatal1 = num1 + num2
print('点数和为：%d' %tatal1)
if tatal1 == 7 or tatal1 == 11:
    print('玩家胜！')
elif tatal1 == 2 or tatal1 == 3 or tatal1 == 12:
    print('电脑胜!')
else:
    go_on = True
while go_on:
    num3 = int(randint(1,6))
    num4 = int(randint(1,6))
    tatal2 = num3 + num4
    print('点数和为：%d' %tatal2)
    if tatal1 == tatal2:
        print('玩家胜！')
        go_on = False
    elif tatal2 == 7:
        print('电脑胜！')
        go_on = False