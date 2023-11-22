n,m =  map(int,input().split())

listen = set()
see = set()

# 듣도 못한 사람 입력
for _ in range(n):
    listen.add(input())

# 보도 못한 사람 입력
for _ in range(m):
    see.add(input())

# 두 집합의 교집합을 저장
common_values = sorted(list(listen.intersection(see)))

print(len(common_values))
for i in common_values:
    print(i)
