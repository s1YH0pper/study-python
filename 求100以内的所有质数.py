from time import *

begin = time()

# 求100以内的所有质数
# 方法一：
# print('2')
# a = 1
# while a < 10000 :
#     a += 2
#     b = 2
#     flag = True
#     while b <= a ** 0.5 :
#         if a % b == 0 :
#             flag = False
#             break
#         b += 1
#     if flag :
#         print(a)

a = 2
while a < 100000 :
    b = 2
    flag = True
    if a % 2 == 0 and a != 2 :
        a += 1
        continue
    else :
        while b <= a ** 0.5 :
            if a % b == 0 :
                flag = False
                break
            b += 1
        if flag :
            print(a)
    a += 1

end = time()
print(end - begin)