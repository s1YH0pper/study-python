import random

def miller_rabin(n, k=5):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_primes(n):
    f = open('output.txt', 'w')
    a = 2
    while a < n:
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
            if flag and miller_rabin(a):
                print(a)
                f.write(str(a) + '\n')
        a += 1
    f.close()


if __name__ == '__main__':
    n = int(input("请输入一个正整数："))
    find_primes(n)
    print("结果已经输出到output.txt文件中。")