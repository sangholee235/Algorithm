
n = int(input())
array = []

for _ in range(n):
    a = int(input())

    if a == 0:
        array.pop()

    else:
        array.append(a)

print(sum(array))



