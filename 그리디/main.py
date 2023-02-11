if __name__ == '__main__':
    N, M = map(int, input().split())
    books = list(map(int, input().split()))
    answer = 0
    weight = 0

    if N == 0:
        print(answer)
    else:
        for i in books:
            if i + weight > M:
                weight = i
                answer += 1
            else:
                weight += i

    print(answer)