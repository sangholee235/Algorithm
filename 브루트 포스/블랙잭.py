n,m = map(int,input().split())

card = list(map(int,input().split()))

answer = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] > m:
                continue
            else:
                answer = max(answer,card[i]+card[j]+card[k])

print(answer)