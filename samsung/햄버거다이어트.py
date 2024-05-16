T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())

    # 점수, 칼로리
    s = []
    k = []


    def dfs(i, taste, kcal):
        global answer
        if kcal > L:  # 칼로리가 리미트를 넘으면
            return
        if taste > answer:
            answer = taste
        if i == N:
            return
        dfs(i + 1, taste + s[i], kcal + k[i])
        dfs(i + 1, taste, kcal)


    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)

    answer = 0

    dfs(0, 0, 0)

    print("#" + str(tc) + " " + str(answer))
