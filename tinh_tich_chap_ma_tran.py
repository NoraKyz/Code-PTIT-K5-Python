T = int(input())  # Số lượng bộ test

for _ in range(T):
    N, M = map(int, input().split())  # Kích thước ma trận ảnh (N x M)
    image = []  # Khởi tạo ma trận ảnh

    # Đọc dữ liệu ma trận ảnh
    for _ in range(N):
        row = list(map(int, input().split()))
        image.append(row)

    kernel = []  # Khởi tạo ma trận kernel

    # Đọc dữ liệu ma trận kernel
    for _ in range(3):
        row = list(map(int, input().split()))
        kernel.append(row)

    # Thực hiện phép nhân tích chập
    result = []
    
    for i in range(1, N - 1):
        row_result = []
        for j in range(1, M - 1):
            sub_matrix = [image[i - 1][j - 1], image[i - 1][j], image[i - 1][j + 1],
                          image[i][j - 1], image[i][j], image[i][j + 1],
                          image[i + 1][j - 1], image[i + 1][j], image[i + 1][j + 1]]
            convolution = sum(sub_matrix[k] * kernel[k // 3][k % 3] for k in range(9))
            row_result.append(convolution)
        result.append(row_result)

    # In kết quả cho bộ test hiện tại
    for row in result:
        print(*row)