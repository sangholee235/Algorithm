n,m = map(int,input().split())

monster = []

for i in range(1,n+1):
    name = str(input())
    monster.append(name)


for name in monster:

    if name == 'Sangho':
        print(name)


print(monster)
