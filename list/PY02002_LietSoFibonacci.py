f = [0, 1, 1]
for i in range(3, 93):
    f.append(f[i-1] + f[i-2])
for t in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print(*f[a:b+1])