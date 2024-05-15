T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())

    max_flavor = 0

    hamburgers = [list(map(int, input().split())) for _ in range(N)]

    hamburgers = sorted(hamburgers, key=lambda x: x[1])

    for i in hamburgers:
        i[1]

    print(hamburgers)
