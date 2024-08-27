def check(s):
    if len(s) % 2 == 0 or s[0] == s[1]:
        return False
    for i in range(2, len(s), 2):
        if s[i] != s[0]: 
            return False
    return True
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        if check(s): 
            print("YES")
        else: 
            print("NO")