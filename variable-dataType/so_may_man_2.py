def tachSo(n):
    while n > 0:
        if n % 10 != 4 and n % 10 != 7:
            return False
        n //= 10
    return True

if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        if tachSo(n):
            print("YES")
        else:
            print("NO")