from collections import deque

# 행과 열의 개수 입력 받음
n = int(input())

matrix = []

# 안전영역 초기화 (비 안올때는 다 안잠기니까 최소 1은 확보)
max_safe = 1

# 방향벡터 초기화
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 영역의 높이 입력 받기
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

heights = set()
for row in matrix:
    heights.update(row)

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

# 높이별 차감
for i in heights:
    new_matrix = [row[:] for row in matrix]  # 새로운 매트릭스 생성
    safearea = 0

    # 물에 잠겼는지 안잠겼는지 확인 반복문
    for x in range(n):
        for y in range(n):
            # 물에 잠겼으면 0
            if (new_matrix[x][y] - i) <= 0:
                new_matrix[x][y] = 0
            # 안잠겼으면 1로 초기화
            else:
                new_matrix[x][y] = 1

    # 새로운 매트릭스에서 bfs 수행
    for x in range(n):
        for y in range(n):
            if new_matrix[x][y] == 1:
                bfs(new_matrix, x, y)
                safearea += 1

    # 수행 후 안전영역 크기 비교 후 초기화
    if max_safe < safearea:
        max_safe = safearea

print(max_safe)
