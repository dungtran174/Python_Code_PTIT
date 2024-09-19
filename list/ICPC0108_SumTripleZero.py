for _ in range(int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    ans = 0
    for i in range(0, n - 2):
        l, r = i + 1, n - 1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                ans += 1
                l += 1
            elif a[i] + a[l] + a[r] < 0:
                l += 1
            else:
                r -= 1
    print(ans)