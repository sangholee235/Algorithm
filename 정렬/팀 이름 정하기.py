#연두 이름 입력 받기
name = str(input())

n = int(input())

team = []
rate = []

L = name.count('L')
O = name.count('O')
V = name.count('V')
E = name.count('E')

for i in range(1,n):
    team[i] = str(input())

for i in range(team):
    L += team[i].count('L')
    O += team[i].count('O')
    V += team[i].count('V')
    E += team[i].count('E')

    rate[i] = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    L -= team[i].count('L')
    O -= team[i].count('O')
    V -= team[i].count('V')
    E -= team[i].count('E')


rate.sort()

for i in range(team):
    L += team[i].count('L')
    O += team[i].count('O')
    V += team[i].count('V')
    E += team[i].count('E')

    if rate[0] == ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100:
       print(team[i])
       break

    L -= team[i].count('L')
    O -= team[i].count('O')
    V -= team[i].count('V')
    E -= team[i].count('E')

