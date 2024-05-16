T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    kill = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for k in range(M):
                for l in range(M):
                    kill += fly[i + k][j + l]

            if kill > max_kill:
                max_kill = kill
                kill = 0
            else:
                kill = 0

    print("#" + str(tc) + " " + str(max_kill))
