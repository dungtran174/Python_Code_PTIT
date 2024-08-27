if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        tich, sum, ok = 1, 0, 0
        for i in range(len(n)):
            if i % 2 == 0:
                if n[i] != '0':
                    tich *= int(n[i])
                    ok = 1
            else:
                sum += int(n[i])
        if ok == 0:
            tich = 0
        print(tich, sum)