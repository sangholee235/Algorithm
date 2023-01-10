n = int(input())

list = []

for i in range(n):
    a = int(input())
    list.append(a)

list.sort()

for i in range(len(list)):
    print(list[i])
