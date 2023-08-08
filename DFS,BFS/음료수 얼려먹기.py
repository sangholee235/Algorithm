# 얼음틀의 세로길이 n, 가로길이 m 입력 받기 
n,m = map(int,input().split())

graph = []

# 아이스크림 틀 입력받기
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y <= m:
        return False

