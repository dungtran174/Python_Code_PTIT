import heapq
import re

t = int(input())
for z in range(t):
    n = int(input())
    main = " " + input().replace(" ", "  ") + " "
    a = []
    i = -8
    while i < 9 and len(a) < 4:
        s = "\d" * abs(i) + " "
        if i < 0:
            s = "-" + s
        elif i > 0:
            s = " " + s
        else:
            i += 1
            continue
        a += [int(x) for x in re.findall(s, main)]
        i += 1
    ans = 0
    for x in heapq.nsmallest(3, a):
        ans += x
    print(ans)
