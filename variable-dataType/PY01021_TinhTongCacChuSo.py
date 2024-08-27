t = int(input())
for _ in range(t):
    n = input()
    sum = []
    k = 0
    for i in n:
        if i.isalpha():
            sum.append(i)
        elif i.isdigit():
            k += int(i)
    # sum.sort()
    a = "".join(sorted(sum))
    print(a + str(k))