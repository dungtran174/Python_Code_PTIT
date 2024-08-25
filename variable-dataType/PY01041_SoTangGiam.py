def solve(s):
    if len(s) < 3:
        return False
    ar = list(int(i) for i in s)
    up = True
    for i in range(1, len(ar)):
        if up and ar[i] <= ar[i - 1]:
            up = False
        elif not up and ar[i] >= ar[i - 1]:
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if solve(s) else "NO")
