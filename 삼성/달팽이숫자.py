T = int(input())

# 방향 설정 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 테스트 케이스만큼
for tc in range(1, T + 1):
    # 달팽이 크기
    n = int(input())

    # 달팽이 리스트 초기화
    snail = [[0] * n for _ in range(n)]

    x, y = 0, 0

    dist = 0

    for i in range(1, n * n + 1):
        snail[x][y] = i

        x += dx[dist]
        y += dy[dist]

        if x < 0 or y < 0 or x >= n or y >= n or snail[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]

            dist = (dist + 1) % 4

            x += dx[dist]
            y += dy[dist]

    print("#" + str(tc))

    for j in snail:
        print(*j)
    print()
