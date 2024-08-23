if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b = []
        n = str(input())
        for i in range(1, len(n)):
            if n[i].isdigit():
                for _ in range(int(n[i])):
                    b.append(n[i-1])
        print(*b, sep='')
        