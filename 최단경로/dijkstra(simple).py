import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n,m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어있는 연결 정보 확인
graph = [[] for _ in range(n + 1)]

# 방문 여부 초기화
visited = [False] * (n + 1)

# 거리 무한대로 초기화
distance = [INF] * (n + 1)

# 간선의 개수 만큼 입력받자
for _ in range(m):
    # a 노드에서 b까지는 c의 비용이 든다
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환한다.
def get_smallest_node():
    min_value = INF 
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]: # 방문하지 않았으면서 현재 최솟값보다 작은 경우
            min_value = distance[i] # 최소거리 갱신
            index = i # 인덱스 정보 저장

    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해서 초기화를 한다
    distance[start] = 0 
    # 방문처리
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작노드를 제외한 전체 n-1개 노드 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 연결된 노드와 
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    
    else:
        print(distance[i])

        

