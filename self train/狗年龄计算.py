num = int(input('请输入狗狗狗的年龄：'))
if num < 0:
    print('你家狗还没出生呢！')
if num <= 2:
    print('你家的狗', num * 10.5, '岁了')
else:
    print('你家的狗', 21 + (num - 2) * 4, '岁了')
