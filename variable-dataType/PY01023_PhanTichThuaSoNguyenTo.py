from math import *
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("1", end = '')
        for i in range(2, int(sqrt(n)) + 1):
            mu = 0
            while(n % i == 0):
                mu += 1
                n //= i
            if mu > 0:
                print(" * ", end = '')
                print(f"{i}^{mu}", end = '')
        if n > 1:
            print(f" * {n}^1", end = '')
        print()