def to_base_k(n, k):
    """Chuyển đổi số n từ hệ thập phân sang hệ cơ số k."""
    digits = []
    while n > 0:
        digits.append(n % k)
        n //= k
    return digits[::-1]

def is_palindrome(lst):
    """Kiểm tra xem danh sách lst có phải là palindrome hay không."""
    return lst == lst[::-1]

def is_palindromic_in_all_bases(n, M):
    """Kiểm tra xem số n có phải là số thuận nghịch trong tất cả các cơ số từ 2 đến M hay không."""
    for k in range(2, M + 1):
        if not is_palindrome(to_base_k(n, k)):
            return False
    return True

def count_palindromic_numbers(a, b, M):
    """Đếm số lượng các số trong đoạn [a, b] là thuận nghịch trong tất cả các cơ số từ 2 đến M."""
    count = 0
    for n in range(a, b + 1):
        if is_palindromic_in_all_bases(n, M):
            count += 1
    return count

def main():
    # Đọc giá trị a, b và M từ đầu vào
    a, b, M = map(int, input().split())
    # Đếm số lượng các số thỏa mãn điều kiện
    result = count_palindromic_numbers(a, b, M)
    # In ra kết quả
    print(result)

if __name__ == "__main__":
    main()