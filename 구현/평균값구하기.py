T = int(input())

for test_case in range(1, T + 1):
    num_arr = []

    num_arr = list(map(int, input().split()))

    avg = sum(num_arr) / 10
    avg = round(avg)

    print("#" + str(test_case) + " " + str(avg))
