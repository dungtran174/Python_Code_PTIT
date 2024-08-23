def check_distance(s1):
    s2 = s1[::-1]  # Đảo ngược xâu s1 để tạo s2
    n = len(s1)
    for i in range(1, n):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return "NO"
    return "YES"
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input().strip()
        print(check_distance(s1))