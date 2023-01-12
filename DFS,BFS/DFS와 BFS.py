# 정점, 간선, 시작정점
vertex_num, edge, start = map(int,input().split())
new_graph = [[]*2 for _ in range(edge)]
graph = [[0]*2 for _ in range(edge)]

for i in range(edge):
    graph[i] = list(map(int,input().split()))

print(graph)

for i in graph:
    index = i[0]
    value = i[1]
    new_graph[index].append(value)

def dfs():

def bfs():


print(new_graph)






