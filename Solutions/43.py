for i in range(1,100):
    disarium = i
    isDisarium = 0
    power = len(str(disarium))

    while disarium != 0:
        ld = disarium % 10
        isDisarium += ld**power
        power -= 1
        disarium //= 10

    if isDisarium==i:
        print(isDisarium)