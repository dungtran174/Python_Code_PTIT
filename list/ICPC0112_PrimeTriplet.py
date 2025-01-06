from math import sqrt

MAX = int(1e6 + 5)
p = [1] * MAX
p[0] = p[1] = 0
for i in range(2, int(sqrt(MAX)) + 1):
    if p[i]:
        for j in range(i * i, MAX, i):
            p[j] = 0

for i in range(int(input())):
    cnt = 0
    for j in range(int(input()) - 5):
        if p[j] and (p[j + 2] or p[j + 4]) and p[j + 6]:
            cnt += 1
    print(cnt)
