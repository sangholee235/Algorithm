n = int(input())

#2차원 리스트 초기화
meet = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int,input().split())
    meet[i][0] = start
    meet[i][1] = end

#제일 중요한 포인트 -> 정렬 우선순서 끝나는시간우선 -> 시작시간 우선
meet.sort(key=lambda x:x[0]) # 시작 시간 정렬
meet.sort(key=lambda x:x[1]) # 끝나는 시간 정렬

count = 1
end = meet[0][1] # 정렬된 첫번째 미팅 끝나는 시간으로 초기화

for i in range(1,n):
    # 시작시간이 끝나는 시간보다 크거나 같다면
    if meet[i][0] >= end:
       count += 1
       # 끝나는 시간을 현재 회의의 끝나는 시간으로 세팅
       end = meet[i][1]

print(count)


#1 10
#2 3
#3 4
#4 5

