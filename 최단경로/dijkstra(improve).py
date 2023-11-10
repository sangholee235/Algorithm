import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드개수, 간선개수 입력받기
n,m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]

# 최단거리 테이블 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a에서 b로가는 비용이 c

def dijkstra(start):
    q = []
    # 시작으로 가는 비용은 0으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 거리와 현재노드 뽑기
        dist, now = heapq.heappop(q)
        # 이미 현재 거리가 더 짧다면 (이미 처리됐다면) 
        # 거리 리스트[현재노드] < 우선순위 큐에서 나온 dist,now
        if distance[now] < dist:
            continue
        # now (현재 노드번호)에 인접한 모든 노드를 돌며
        for i in graph[now]:
            # 비용 = 우선순위 큐에서 나온 거리 + 노드와 연결된 것 중 하나의 거리
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 그걸로 바꿈
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 우선순위 큐에 넣는다, (현재 비용, 노드번호) 쌍을
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF: # 거리가 무한대면 예외처리
        print("INFINITY")
    else:
        print(distance[i])

