from collections import deque

# 정점, 간선, 시작정점  개수
vertex_num, edge, start = map(int,input().split())
new_graph = [[]*2 for _ in range(vertex_num)]
graph = [[0]*2 for _ in range(edge)]
dfs_list = []
bfs_list = []

# 방문기록 변수
visited = [False]*(vertex_num+1)

for i in range(edge):
    graph[i] = list(map(int,input().split()))

for i in graph:
    new_graph[i[0]].append(i[1])

print(new_graph)

def dfs(g,v,visited):
    visited[v] = True
    dfs_list.append(v)

    for i in g[v]:
        if not visited[i]:
           dfs(g,v,visited)

dfs(new_graph,start,visited)

print(dfs_list)





