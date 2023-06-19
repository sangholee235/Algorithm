n = int(input()) # 사람의 수

t = list(map(int,input().split())) # 인출하는데 걸리는 시간

t.sort() # 오름차순으로 정렬

sum = 0

for i in t:
    sum += 2*i

print(sum)
