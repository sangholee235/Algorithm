import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

while True:
    m,n = map(int, input().split())

    if n == 0 and m == 0:
        break

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
           return False

        if graph[x][y] == 1:  # Check if the cell is land (1), not water (0)
           graph[x][y] = 0   # Mark the cell as visited
  
           dfs(x - 1, y)
           dfs(x, y - 1)
           dfs(x + 1, y)
           dfs(x, y + 1)
           dfs(x - 1, y - 1)
           dfs(x - 1, y + 1)
           dfs(x + 1, y - 1)
           dfs(x + 1, y + 1)
           return True
             
        return False

    graph = []

    for _ in range(n):
        graph.append(list(map(int, read().split())))

    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)
