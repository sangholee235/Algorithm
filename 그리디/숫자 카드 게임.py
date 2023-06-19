n,m = map(int,input().split())

result = 0

for i in range(n): # 행의 개수 만큼 돈다
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)
