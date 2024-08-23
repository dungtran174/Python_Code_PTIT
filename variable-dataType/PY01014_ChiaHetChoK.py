if __name__ == '__main__':
    b = []
    a, k, n = map(int, input().split())
    st = k - a % k
    end = n - a
    while st <= end:
        b.append(st)
        st += k     
    if(len(b) == 0):
        print(-1)
    else:
        print(*b)