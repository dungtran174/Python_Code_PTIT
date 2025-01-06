for i in range (int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            break
    else:
        print("YES")