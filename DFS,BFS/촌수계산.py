n = int(input())

a,b = map(int, input().split())

m = int(input())

g = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
answer = []

# 2차원 그래프에 노드 정보 저장 ( m 만큼 )
for _ in range(m):
    x,y = map(int,input().split())
    g[x].append(y)
    g[y].append(x)


def dfs(vertex, count):
    # 촌수 늘리기
    count += 1
    # 방문 여부 체크
    visited[vertex] = True

    # 요구한 사람이 닿으면 촌수 입력
    if vertex == b:
       answer.append(count)

    # 그래프를 돌며
    for i in g[vertex]:
        # 방문 한적이 없다면 탐색
        if not visited[i]:
           dfs(i,count)

dfs(a,0)

# 촌수를 찾을 수 없을 경우
if len(answer) == 0:
   print(-1)

else:
    print(answer[-1]-1)
