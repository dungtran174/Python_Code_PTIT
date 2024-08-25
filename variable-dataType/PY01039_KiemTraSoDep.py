def check(s):
    for i in range(2, len(s)):
        if s[i] != s[i - 2]:
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print('YES' if check(s) else 'NO')