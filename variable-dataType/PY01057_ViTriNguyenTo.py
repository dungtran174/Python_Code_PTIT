def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    for i in range(len(s)):
        if nto(i) != nto(int(s[i])):
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = input()
        if check(n):
            print("YES")
        else:
            print("NO")
