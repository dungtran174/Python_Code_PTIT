for _ in range(int(input())):
    n = input()
    for i in n:
        if i.isalpha():
            n = n.replace(i, ' ')
    n = [int(i) for i in n.split()]
    print(min(n))