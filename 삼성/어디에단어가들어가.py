T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or j == N - 1:
                if count == K:
                    answer += 1
                count = 0

    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or i == N - 1:
                if count == K:
                    answer += 1
                count = 0

    print("#" + str(tc) + " " + str(answer))
