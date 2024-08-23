if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = str(input())
        k = n[0:2]
        h = n[-2:]
        if k == h:
            print("YES")
        else:
            print("NO")
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         dem = len(str(n))
#         k = n % 100
#         h = n // (10 ** (dem-2))   
#         if k == h:
#             print("YES")
#         else:
#             print("NO") 