n, m = map(int, input().split())
tree = list(map(int, input().split()))

first = 1
last = max(tree)

while first <= last:
    mid = (first + last) // 2
    sum = 0

    for i in tree:
        if i >= mid:
            sum += i - mid

    # 나무가 더 짤림 그러므로 절단기 커트를 올려야함
    if sum >= m:
        first = mid + 1
    # 나무가 덜 짤림 절단기 커트를 내려야 함
    else:
        last = mid - 1

print(last)


