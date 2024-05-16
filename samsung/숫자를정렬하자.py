T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    arr.sort()

    print("#" + str(tc), end=" ")

    for number in arr:
        print(number, end=" ")

    print()
