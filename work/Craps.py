from random import randint
money = 1000
while money >0:
    print('玩家总资产：%d' % money)
    while True:
        debt = int(input('清下注：'))
        if 0 < debt <= money:
            break
    go_on = False
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    total1 = num1 + num2
    print('玩家摇出了%d' % total1)
    if total1 == 7 or total1 == 11:
        print('玩家胜')
        money += debt
    elif total1 == 2 or total1 == 3 or total1 == 12:
        print('玩家输')
        money -= debt
    else:
        go_on = True
    while go_on:
        num1 = randint(1, 6)
        num2 = randint(1, 6)
        total2 = num1 + num2
        print('玩家摇出了%d' % total2)
        if total2 == total1:
            print('玩家胜!')
            money += debt
            go_on = False
        elif total2 == 7:
            print('玩家输!')
            money -= debt
            go_on = False
print('你已经破产！')
#     #21根火柴，每次最少一根，最多4根，玩家必须拿到最后一根，必须输。
#
#
