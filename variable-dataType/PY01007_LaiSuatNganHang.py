if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a, b, c = map(float, input().split())
        dem = 0
        while a < c:
            a += a * b / 100
            dem += 1
        print(dem)

    