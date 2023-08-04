from collections import deque

# 정점의 개수, 간선의 개수, 탐색을 시작할 정점
vertex_num, edge, start = map(int,input().split())

# 입력 받을 그래프 리스트임
graph = [[0]*2 for _ in range(edge)]

# 그래프 변환용 리스트
new_graph = [[]*2 for _ in range(vertex_num+1)]

# 방문 여부 체크용 1차원 리스트!
visited = [False] * (vertex_num+1)

# 사용자에게 그래프 입력 받기
for i in range(edge):
    graph[i] = list(map(int,input().split()))

# 그래프 변환
for i in graph:
    new_graph[i[0]].append(i[1])

# (그래프, 시작 정점, 방문 여부)
def dfs(g,v,visited):
    visited[v] = True
    print(v,end=' ')

    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)

def bfs(g,started,visited):
    queue = deque([started])
    visited[started] = True

    while queue:
        v= queue.popleft()
        print(v, end=' ')

        for i in g[v]:
            if not visited[i]:
               queue.append(i)
               visited[i] = True


dfs(new_graph,start,visited)
visited = [False] * (vertex_num+1)
print(sep='\n')
bfs(new_graph,start,visited)
