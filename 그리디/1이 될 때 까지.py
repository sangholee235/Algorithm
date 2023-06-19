n,k = map(int,input().split())
result = 0

while n >= k: # n이 k 이상 이라면 반복한다
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1 # 계산 횟수 증가 시키기

    # 나누어 떨어진다면
    n //= k # k로 나누기
    result += 1 # 계산 횟수 증가 시키기

# 남은 수에 대하여 1씩 빼기 ex) n=2 k=3 인 상황에서 n을 1로 만들기 위해
while n > 1:
    n -= 1
    result += 1

print(result)