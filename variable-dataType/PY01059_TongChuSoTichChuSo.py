if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        sum, ok, tich = 0, 0, 1
        for i in range(len(n)):
            if i % 2 == 0:
                sum += int(n[i])
            else:
                if n[i] != "0":
                    tich *= int(n[i])
                    ok = 1
        if ok == 0:
            tich = 0
        print(sum, tich)
