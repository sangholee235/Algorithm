import sys

input = sys.stdin.readline

n,m = map(int,input().split())

dict = {}

for _ in range(1,n+1):
    a,b = input().split()
    dict[a] = b

for _ in range(m):
    quest = input().rstrip()

    print(dict[quest])