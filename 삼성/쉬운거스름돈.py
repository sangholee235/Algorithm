T = int(input())

moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T + 1):
    N = int(input())

    shares = []

    for money in moneys:
        shares.append(N // money)
        N = N % money

    print("#" + str(tc))
    for share in shares:
        print(share, end=" ")

    print()
