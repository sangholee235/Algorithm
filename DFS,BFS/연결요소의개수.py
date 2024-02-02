import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 연결요소 이다
count = 0

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1,n+1):
    if visited[i] == 0:
        if not graph[i]:
           count += 1
           visited[i] = 1
        else:
            bfs(i)
            count += 1

print(count)
