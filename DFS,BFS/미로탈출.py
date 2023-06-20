from collections import deque

n,m = map(int,input().split())

graph = [] # 그래프 선언

dx = [-1,1,0,0] # x좌표의 움직임 리스트
dy = [0,0,1,-1] # y좌표의 움직임 리스트

for i in range(n):
    graph.append(list(map(int,input().split())))

