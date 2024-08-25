from math import *
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = str(input())
        k = n[::-1]
        if (gcd(int(k),int(n)) == 1):
            print("YES")
        else:
            print("NO")