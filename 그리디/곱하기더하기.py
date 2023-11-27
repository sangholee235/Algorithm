arr = list(map(int,input()))

result = 1

for i in arr:
    if int(i) == 0:
        result -= 1
    elif int(i) == 1:
        continue
    else:
        result = result * i

print(result)
