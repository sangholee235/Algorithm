
m,l = int(input.split())
array = list(map(int,input().split()))

# 물이 새는 위치 정렬
array.sort()

start = array[0] # 물이 처음 터진 부분 부터 테이프를 붙인다
count = 1 # 테이프 개수 초기화 하나는 써야되니까?

for location in array[1:]: # 처음을 제외하고 다음 물새는 위치부터 반복문 돌기
    if location in (start, start + l):
        continue
    else:
        # 시작 지점을 지금 물새는 위치로 바꿔주고 테이프 개수 추가
        start  = location
        count += 1

print(count)