import sys

input = sys.stdin.readline

n,m = map(int,input().split())

monster = []

# 포켓몬이름 입력받는 모듈
for i in range(1,n+1):
    name = str(input())
    monster.append(name)

for _ in range(m):
    quest = input().rstrip()




def hash(quest):
  for name in monster:
     
      if quest.isdigit():
         print(name)


print(monster)
