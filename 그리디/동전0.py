n,k = map(int,input().split())

money = list()

for i in range(n):
    money.append(int(input()))

money.reverse()
# 화폐를 내림차순으로 바꿈

count = 0

for i in money:
    count += k // i  # 나눠진 만큼 카운팅
    k %= i  # 나눠진 나머지를 화폐값으로 저장

print(count)




