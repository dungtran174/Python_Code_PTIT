if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = 0
        for i in range(2 - n % 2, n + 1, 2):
            s += 1 / i
        print(f"{s:.6f}")
            
            