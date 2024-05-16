T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    max_value = max(arr)
    min_value = min(arr)

    arr.remove(max_value)
    arr.remove(min_value)

    avg_value = sum(arr) / len(arr)

    avg_value = round(avg_value)

    print("#" + str(tc) + " " + str(avg_value))
