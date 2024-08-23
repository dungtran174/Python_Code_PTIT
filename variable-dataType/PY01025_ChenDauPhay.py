if __name__ == '__main__':
    n = input()
    for i in range(len(n) - 3, 0, -3):
        n = n[:i] + ',' + n[i:]
    print(n)
    