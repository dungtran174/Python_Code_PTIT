from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    for i in n:
        if not is_prime(int(i)):
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    m = int(str(n)[::-1])
    s = sum([int(i) for i in str(n)])
    if is_perfect(str(n)) and is_prime(n) and is_prime(m) and is_prime(s):
        print('Yes')
    else:
        print('No')