def check(n):
    if sum(int(i) for i in n) % 10 != 0:
        return False
    for i in range (0, len(n) - 1):
        if(abs(ord(n[i]) - ord(n[i + 1])) != 2):
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        n = input()
        if(check(n)):
            print("YES")
        else:
            print("NO")