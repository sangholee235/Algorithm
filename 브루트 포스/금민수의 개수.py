a,b = map(int,input().split())
nums = [4,7]
count = 0

for i in (a,b+1):
    s = str(i)

    if '0' in s or '1' in s or '2' in s or '3' in s or '5' in s or '6' in s or '8' in s or '9' in s:
        continue

    count += 1

print(count)


