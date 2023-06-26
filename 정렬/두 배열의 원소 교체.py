n,k = int(input().split())

a = []
b = []

a.sort()
sorted(b,reverse=True)

for i in range(k):
    if a[k]<b[k]:
        a[k],b[k] = b[k],a[k]
    else:
        break

print(sum(a))