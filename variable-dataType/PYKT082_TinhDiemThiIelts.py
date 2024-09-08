def trans(n):
    if n >= 39:
        return 9
    if n >= 37:
        return 8.5
    if n >= 35:
        return 8
    if n >= 33:
        return 7.5
    if n >= 30:
        return 7
    if n >= 27:
        return 6.5
    if n >= 23:
        return 6
    if n >= 20:
        return 5.5
    if n >= 16:
        return 5
    if n >= 13:
        return 4.5
    if n >= 10:
        return 4
    if n >= 7:
        return 3.5
    if n >= 5:
        return 3
    if n >= 3:
        return 2.5


t = int(input())
for i in range(t):
    a = input().split()
    r, l = int(a[0]), int(a[1])
    s, w = float(a[2]), float(a[3])
    x = (trans(r) + trans(l) + s + w) / 4.0
    if x - int(x) >= 0.75:
        print(int(x) + 1.0)
    elif x - int(x) >= 0.25:
        print(int(x) + 0.5)
    else:
        print(int(x) + 0.0)
# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0
