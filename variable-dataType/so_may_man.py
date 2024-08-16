def dem(n):
    cnt = 0
    while n > 0:
        if n % 10 == 7 or n % 10 == 4:
            cnt += 1
        n //= 10
    return cnt

if __name__ == '__main__':
    n = int(input())
    if dem(n) == 4 or dem(n) == 7:
        print("YES")
    else:
        print("NO")
    