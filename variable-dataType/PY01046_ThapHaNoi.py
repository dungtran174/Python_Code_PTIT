def thap_ha_noi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    # Di chuyển n-1 đĩa từ cọc A sang cọc B, dùng cọc C làm trung gian
    thap_ha_noi(n - 1, a, c, b)

    # Di chuyển đĩa cuối cùng từ cọc A sang cọc C
    print(a, "->", c)

    # Di chuyển n-1 đĩa từ cọc B sang cọc C, dùng cọc A làm trung gian
    thap_ha_noi(n - 1, b, a, c)

# Số lượng đĩa
n = int(input())
if __name__ == "__main__":  
    thap_ha_noi(n, 'A', 'B', 'C')