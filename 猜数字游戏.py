import random

aim_number = random.randint(1, 100)

while True:
    try:
        guess_number = int(input("请猜一个1到100之间的整数："))
    except ValueError:
        print("输入的值不是整数，请重新输入！")
        continue
    if aim_number < guess_number:
        limit = guess_number - aim_number
        tip = random.randint(1, limit)
        print('你猜的数字偏大了,至少大了%s' % tip)
    elif aim_number > guess_number:
        limit = aim_number - guess_number
        tip = random.randint(1, limit)
        print('你猜的数字偏小了,至少小了%s' % tip)
    else:
        print('恭喜你猜对了')
        break
