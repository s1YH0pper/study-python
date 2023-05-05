a = 1
while a < 10:
    b = 1
    while b <= a:
        print(b, '*', a, '=', a * b, end='  ')
        b += 1
    print()
    a += 1
