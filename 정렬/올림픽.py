#국가의 수 , 등 수를 알고 싶은 국가의 번째
n, k = map(int,input().split())
a = []

for i in range(n):
    a.append(list(map(int,input().split())))

#메달로 등수 정렬
a.sort(key=lambda x:(-x[1],-x[2],-x[3]))

# 등 수를 알고 싶은
for i in range(n):
    if a[i][0] == k:
       index = i

# 국가 출력
for i in range(n):
    # 국가 구분이후의 메달 구분
    if a[index][1:] == a[i][1:]:
       print(i+1)
       break
