n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

S = sum(a * b for a,b in zip(a,b))

print(S)