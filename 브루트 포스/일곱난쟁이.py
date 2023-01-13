nj = []
diff = 0

for i in range(9):
    nj.append(int(input()))

diff = sum(nj) - 100

for i in range(9):
    for j in range(9):
        if nj[i] != nj[j]:
           if nj[i]+nj[j] == diff:
              nj.pop(i)
              nj.pop(j)

nj.sort()

for i in range(7):
    print(nj[i])


