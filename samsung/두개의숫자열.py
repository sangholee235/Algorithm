T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) > len(B):
        B, A = A, B

    arr = []

    for i in range(len(B) - len(A) + 1):
        sum = 0
        for j in range(len(A)):
            sum += A[j] * B[j + i]
        arr.append(sum)

    answer = max(arr)

    print("#" + str(tc) + " " + str(answer))
