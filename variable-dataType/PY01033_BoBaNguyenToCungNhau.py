from math import gcd
if __name__ == '__main__':
    l, r = [int(x) for x in input().split()]
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            for k in range(j + 1, r + 1):
                if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(i, k) == 1:
                    print("(" + str(i) + ", " + str(j) + ", " +  str(k) + ")")