sum = int(input('输入一个大于1的自然数'))
i = 2
flag = True
while i < sum :
    if sum % i == 0 :
        i += sum
        flag = False
    else :
        i += 1

if flag :
    print('你输入的是一个质数')
else :
    print('你输入的是一个素数')