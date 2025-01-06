n = int(input())
res = 0
a = [int(x) for x in input().split()]
for i in range(1, n):
    if a[i] != a[i - 1]:
        res += 1
print(res)
