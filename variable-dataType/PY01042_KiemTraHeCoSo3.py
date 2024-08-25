def check(s):
    for i in s:
        if i != '0' and i != '1' and i != '2':
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check(s) else "NO")