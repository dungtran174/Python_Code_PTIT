from math import gcd
from functools import reduce


# Hàm tính GCD của một danh sách số
def find_gcd(arr):
    return reduce(gcd, arr)


def solve():
    T = int(input())  # Đọc số lượng trò chơi

    for _ in range(T):
        n = int(input())  # Đọc số lượng thẻ
        a = list(map(int, input().split()))  # Đọc danh sách bước nhảy
        c = list(map(int, input().split()))  # Đọc danh sách chi phí

        # Tìm GCD của tất cả các bước nhảy
        current_gcd = find_gcd(a)

        # Nếu GCD khác 1, Nam không thể nhảy đến mọi điểm
        if current_gcd != 1:
            print(-1)
            continue

        # Nếu GCD là 1, ta cần tối thiểu chi phí để đạt GCD = 1
        # dp[i] sẽ lưu chi phí tối thiểu để tạo ra GCD = i
        dp = {0: 0}  # Tạo một dict để lưu chi phí, bắt đầu với GCD = 0

        for i in range(n):
            new_dp = dp.copy()
            for g in dp:
                new_g = gcd(g, a[i])
                new_dp[new_g] = min(new_dp.get(new_g, float("inf")), dp[g] + c[i])
            dp = new_dp

        # Kết quả là chi phí tối thiểu để đạt GCD = 1
        if 1 in dp:
            print(dp[1])
        else:
            print(-1)


# Chạy hàm giải quyết
solve()
