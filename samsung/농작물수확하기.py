T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    # ex) 5 // 2 = 2
    half = N // 2

    answer = 0

    for i in range(len(arr)):
        # diff = 2 - 0 = 2
        diff = half - i
        if diff > 0:
            answer += sum(arr[i][diff:-diff])
        elif diff < 0:
            answer += sum(arr[i][-diff:diff])
        else:
            answer += sum(arr[i])

    print("#" + str(tc) + " " + str(answer))
