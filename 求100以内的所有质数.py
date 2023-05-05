from time import *

begin = time()

a = 2
while a < 100000:
    b = 2
    flag = True
    if a % 2 == 0 and a != 2:
        a += 1
        continue
    else:
        while b <= a ** 0.5:
            if a % b == 0:
                flag = False
                break
            b += 1
        if flag:
            print(a)
    a += 1

end = time()
print(end - begin)
