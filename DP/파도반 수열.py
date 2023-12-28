import sys

input = sys.stdin.readline

t = int(input())

d = [0] * (101)

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
d[6] = 3


for i in range(t):
    n = int(input())

    for j in range(7, n + 1):
        d[j] = d[j-1] + d[j-5]

    print(d[n])