for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    k %= n
    print(*(a[k:] + a[:k]))