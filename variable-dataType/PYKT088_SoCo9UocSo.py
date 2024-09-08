n, s, i = int(input()), 0, 2
l = int(n ** (0.5)) + 1
a = [i for i in range(l)]  # a[i] là ước nt của i
for i in range(2, l):
    if a[i] == i:
        for j in range(i * i, l, i):
            if a[j] == j:
                a[j] = i
for i in range(2, l):
    p = a[i]
    q = a[i // a[i]]
    if p * q == i and q != 1 and p != q:  # kiểm tra i là tích của 2 snt
        s += 1
    elif a[i] == i:
        if i**8 <= n:
            s += 1
print(s)
