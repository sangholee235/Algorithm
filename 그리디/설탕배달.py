N = int(input())
# 설탕의 양을 입력 받기

count = 0

while N >= 0: # 설탕 소모 할때 까지 반복
    if N % 5 == 0: # 5키로 단위로 떨어지면 ?
       count += N//5 # 몇개인지 계산한뒤
       print(count) # 바로 출력
       break # 반복문 탈출 끝

    else: # 5개 단위로 떨어지지 않는다면
       N -= 3 # 3키로를 뺴고
       count += 1 # 카운트를 1 증가후 계산 반복문 돎

else:
    print(-1)

count = 0

while N >= 0:
    if N % 5 == 0:
        count += N // 5
        print(count)
        break
    N -= 3
    count += 1

else:
    print(-1)


