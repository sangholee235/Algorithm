import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, sys.stdin.readline().split())

# 2차원 n*m 을 채워넣음
field = [[0 for _ in range(N)] for _ in range(M)] 

for _ in range(K):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    for Y in range(Y1, Y2):
        for X in range(X1, X2):
            field[Y][X] = 1

def dfs(x,y,count):
    field[y][x] = 1
    
    for dx,dy in d:
        X,Y = x + dx , y + dy
        if (0 <= X < N) and (0 <= Y < M) and field[Y][X] == 0:
            count = dfs(X,Y,count+1)
    
    return count

area = []
d = [(0,1),(0,-1),(1,0),(-1,0)]

for Y in range(M):
    for X in range(N):
        if field[Y][X] == 0:
            area.append(dfs(X,Y,count=1))

print(len(area))
print(*sorted(area))

