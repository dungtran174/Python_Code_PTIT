n = int(input())
for i in range(n):
    a = int(input())
    b = {}
    for j in range(a):
        k = int(input())
        if b.get(k):
            b[k] += 1
        else:
            b[k] = 1
    b = sorted(b, key=lambda x : (-b[x], x))
    print(b[0])
    
    