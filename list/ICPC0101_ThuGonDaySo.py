n = int(input())
a = []
b = list(map(int, input().split()))
for i in b:
    if len(a) == 0:
        a.append(i)
    else:
        if (a[-1] + i) % 2 == 0:
            a.pop()
        else:
            a.append(i)
print(len(a))