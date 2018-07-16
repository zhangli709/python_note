fish = 1
while True:
    totle = fish
    is_enough = True
    for _ in range(5):
        if (totle - 1) % 5 == 0:
            totle = (totle - 1 ) // 5 * 4
        else:
            is_enough = False
            break
    if is_enough:
            print(fish)
            break
    fish += 1




