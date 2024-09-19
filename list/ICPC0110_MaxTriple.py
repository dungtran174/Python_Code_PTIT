import heapq
import re
import sys

input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
line_index = 1

for z in range(t):
    n = int(data[line_index])
    main = data[line_index + 1]

    # Sử dụng heap với kích thước 3 để lưu 3 số lớn nhất
    largest = []
    
    # Tìm tất cả các số trong chuỗi `main` (bao gồm cả số âm)
    for num in re.finditer(r'-?\d+', main):
        num = int(num.group())  # Lấy giá trị số từ regex match
        if len(largest) < 3:
            heapq.heappush(largest, num)  # Thêm số vào heap nếu chưa đủ 3 số
        else:
            heapq.heappushpop(largest, num)  # Thay thế số nhỏ nhất nếu số mới lớn hơn

    ans = sum(largest)
    
    print(ans)
    
    line_index += 2
