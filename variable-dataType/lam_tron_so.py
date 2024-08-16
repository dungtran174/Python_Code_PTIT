def round_number(n):
    factor = 10
    while n > factor:
        n = (n + factor // 2) // factor * factor
        factor *= 10
    return n
    
if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        print(round_number(n))
        