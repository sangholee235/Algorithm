T = int(input())

for tc in range(1, T + 1):

    answer = 1

    sdocu = [list(map(int, input().split())) for _ in range(9)]

    # 가로 검사
    for i in range(9):
        num_stack = []
        for j in range(9):
            if sdocu[i][j] in num_stack:
                answer = 0
                break
            else:
                num_stack.append(sdocu[i][j])

    # 세로 검사
    for j in range(9):
        num_stack = []
        for i in range(9):
            if sdocu[i][j] in num_stack:
                answer = 0
                break
            else:
                num_stack.append(sdocu[i][j])

    for k in range(0, 7, 3):
        num_stack = []
        for i in range(k, k + 3):
            for j in range(k, k + 3):
                if sdocu[i][j] in num_stack:
                    answer = 0
                    break
                else:
                    num_stack.append(sdocu[i][j])

    print("#" + str(tc) + " " + str(answer))
