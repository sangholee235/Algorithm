n,c = map(int,input().split())

house = []

for _ in range(n):
    h = int(input())
    house.append(h)

house.sort()

left = 1
right = house[-1] - house[0]

while left<=right:
    mid = (left+right) // 2

print(house)