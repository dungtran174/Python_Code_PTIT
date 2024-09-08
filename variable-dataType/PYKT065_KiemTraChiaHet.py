def is_valid_number(num, N):
    for i in range(2, N + 1):
        if num % i == 0:
            return False
    return True

def count_valid_numbers(L, R, N):
    count = 0
    for num in range(L, R + 1):
        if is_valid_number(num, N):
            count += 1
    return count

def main():
    while True:
        # Đọc giá trị L và R
        L, R = map(int, input().split())
        if L == -1 or R == -1:
            break
        # Đọc giá trị N
        N = int(input())
        # Đếm số lượng các số thỏa mãn điều kiện
        result = count_valid_numbers(L, R, N)
        # In ra kết quả
        print(result)

if __name__ == "__main__":
    main()