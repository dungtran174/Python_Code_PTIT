from math import sqrt
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    for i in range(t) :
        a = list(int(i) for i in input())
        l, nt, ont = len(a), 0, 0
        for i in a:
            if nto(i):
                nt += 1
            else:
                ont += 1
        print("YES" if (nt > ont and nto(l)) else "NO")