if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ok = 1
        for i in range(1000):
            if n % 7 == 0:
                print(n)
                ok = 0
                break
            h = int(str(n)[::-1])
            n += h
        if ok == 1:
            print(-1)
        