T = int(input())

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    arr = []

    for i in range(n):
        mid, final, assign = map(int, input().split())

        score = mid * 0.35 + final * 0.45 + assign * 0.2

        arr.append(score)

    target = arr[k - 1]

    arr.sort(reverse=True)

    rate = n // 10

    ratio = arr.index(target) // rate

    print("#" + str(tc) + " " + str(grades[ratio]))
