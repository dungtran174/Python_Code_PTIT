def ko_giam(n):
    last = n % 10
    n = n // 10
    while n > 0:
        if n % 10 > last:
            return False
        last = n % 10
        n = n // 10
    return True
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if ko_giam(n):
            print('YES')
        else:
            print('NO')