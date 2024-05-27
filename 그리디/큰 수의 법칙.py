n,m,k = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 1

while True:
    for i in range(k): # k번 반복
        if m == 0: # m번 반복이 끝났으면 반복문 탈출
            break
        result += first # 결과 값에 제일 큰 값 더해주기
        m -= 1 # 횟수 차감

    if m == 0: # m번 반복이 끝났으면 반복문 탈출
        break
    result += second # 두 번쨰로 큰 값 ++
    m -= 1 # 횟수 차감

print(result) # 결과값 출력

