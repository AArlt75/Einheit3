for x in range(1, 6):
    print()
    while x > 0:
        if x % 2 != 0:
            zahl = 1
        else:
            zahl = 0
        print(zahl, end="")
        x -= 1