for t in range(int(input())):
    S = sum(int(i) for i in input())
    print('YES' if S > 10 and S == (int(str(S)[::-1])) else 'NO')