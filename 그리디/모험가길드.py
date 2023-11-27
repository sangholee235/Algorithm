n = int(input()) 

member = list(map(int,input().split()))

# 멤버 공포도 오름차순 정렬
member.sort()

# 멤버 카운트
count = 0
# 그룹 카운트
group = 0

for i in member:
    # 인원수 +1
    count += 1

    # 인원수가 공포도를 넘으면
    if count >= i: 
       # 그룹수 증가 (출발)
       group += 1
       # 멤버 수 초기화
       count = 0
       
    else: # 넘지 못한다면 ?
        continue
    
    
print(group)