from math import gcd
if __name__ == '__main__':
    n, k = map(int, input().split())
    h = 10 ** k
    dem = 0
    for i in range(h//10, h):
        if gcd(n, i) == 1:
            print(i, end = " ")
            dem += 1
            if dem % 10 == 0:
                print()                 