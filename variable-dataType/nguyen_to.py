from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def count(n):
    cnt = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            cnt += 1
    return cnt

def check(n):
    k = count(n)
    return prime(k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if check(n):
            print("YES")
        else:
            print("NO")