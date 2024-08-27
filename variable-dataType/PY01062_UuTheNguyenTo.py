def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    for i in range(t) :
        s = input()
        nt, ont = 0 , 0
        for j in s:
            if j in "2357":
                nt += 1
            else:
                ont += 1
        print("YES" if (nt > ont and nto(len(str(s)))) else "NO")