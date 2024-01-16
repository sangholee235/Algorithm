import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

def dfs(n, p):
    visited[n] = p

    for g in graph[n]:
        if visited[g] == 0:
            dfs(g, n)

dfs(1, 1)

for i in range(2, n + 1):
    print(visited[i])
