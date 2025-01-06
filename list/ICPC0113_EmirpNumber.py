from math import sqrt
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    for i in range(2, n):
        j = int(str(i)[::-1])
        if is_prime(i) and is_prime(j) and i < j and j <= n:
            print(i, j, end=' ')
    print()

    