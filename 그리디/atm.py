import sys

input = sys.stdin.readline

n = int(input()) # 사람의 수

t = list(map(int,input().split())) # 인출하는데 걸리는 시간

t.sort() # 오름차순으로 정렬

temp = 0

wait = []

for i in t:
    temp = temp + i
    wait.append(temp)

print(sum(wait))

