# 리스트 크기 입력 받기
n = int(input())

# 지역 리스트 2차원 초기화
area = [[0]*2 for _ in range(n)]

# 안전한 구역 count1
safe = 0

# 현재 강수량
rain = 0

# 지역 정보 입력 받기
for i in range(n):
    area[i] = list(map(int,input().split()))

while 1:
    # 강수량 더해나가기
    for i in range(n):
        for j in range(n):
            area[i][j] += 1





