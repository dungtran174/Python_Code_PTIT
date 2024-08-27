if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        res = 1
        n = input()
        for i in n:
            if i != '0':
                res *= int(i)
        print(res)