n = int(input())

t = []
p = []
dp = [0 for _ in range(n + 1)]

for i in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

# 반복문 거꾸로
for i in range(n - 1, -1, -1):
    if t[i] + i > n:  # 상담일수가 퇴사일을 넘어가는 경우 계산
        dp[i] = dp[i + 1]  # 다음날 값으로

    else:
        # 상담을 할 경우, 안할 경우 중에서 max 값 사용한다
        dp[i] = max(dp[i + 1], dp[t[i] + i] + p[i])

print(dp[0])
