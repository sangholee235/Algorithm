T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    # n*n 리스트를 1로 초기화
    matrix = [[0] * n for _ in range(n)]
    matrix[0][0] = 1

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    print("#" + str(test_case))

    for k in range(n):
        for l in range(n):
            if matrix[k][l]:
                print(matrix[k][l], end=" ")

        print()
