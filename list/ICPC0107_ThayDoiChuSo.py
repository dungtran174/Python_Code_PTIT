for t in range(int(input())):
    n, m = input().split()
    ip = input().split()
    # xử lý nếu đầu vào ghi trên 2 dòng
    if len(ip) == 1:
        str1 = ip[0]
        str2 = input()
    # xử lý nếu đầu vào ghi trên 1 dòng
    else:
        str1, str2 = ip
    num1 = int(str1.replace(n, m)) + int(str2.replace(n, m))
    num2 = int(str1.replace(m, n)) + int(str2.replace(m, n))
    print(min(num1, num2), max(num1, num2))
