from itertools import combinations

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())

    numbers = list(map(int,input().split()))

    for i in range(N):
        number = combinations(numbers,i)
        print(number)