from collections import deque

needs = int(input())

m,n = map(int,input().split())
a = []
b = []
na = []
nb = []
count = 0

for i in range(m):
    a.append(int(input()))

for i in range(n):
    b.append(int(input()))

for i in range(a):
    for j in range(a):
        na.append(a[i::i+j+1])

for i in range(b):
    for j in range(b):
        nb.append(b[i::i+j+1])




