def check(ip):
    for i in ip:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
            return False
    return len(ip) == 4


for i in range(int(input())):
    ip = input().split(".")
    print("YES" if check(ip) else "NO")
