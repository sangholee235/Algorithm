test = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 큐에 삽입
    queue = [(x,y)]
    # 방문 처리
    matrix[x][y] = 0

    while queue:
        # 맨앞에거 뽑아
        x,y = queue.pop(0)
        
        # 네방향 검진
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny > m:
                continue

            # 아직 방문 안했다면
            if matrix[x][y] == 1:
                # 큐에 삽입후
                queue.append((nx,ny))
                # 방문 처리
                matrix[nx][ny] = 0 




for _ in range(test):
    # 가로,세로,배추의개수
    m,n,k = map(int,input().split())
    matrix = [[0] * (n) for _ in range(m)]
    count = 0

    for i in range(k):
        x,y = map(int,input().split())
        matrix[x][y] = 1
    
    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1:
                bfs(a,b)
                count += 1

    print(count)

    