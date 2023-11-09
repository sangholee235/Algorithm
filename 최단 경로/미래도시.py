INF = int(1e9)

n,m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0
            graph[b][a] == 0


# 각 간선에 대한 정보를 입력받아 그값으로 초기화
for _ in range(m): 
    a,b,c = map(int,input().split())
    graph[a][b] = c


# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

