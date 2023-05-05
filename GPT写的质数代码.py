import random
import math
import more_itertools

def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_primes(limit):
    primes = [2]
    for n in range(3, limit + 1, 2):
        if miller_rabin(n):
            primes.append(n)
    return primes

num = int(input("输入一个整数，求出其内的所有质数:"))
primes = find_primes(num)
if len(primes) >= 400 :
    for page in more_itertools.chunked(primes, 20):
        print(page)
        input("按任意键继续...")
else :
    print(primes)