# 공간의 크기
n = int(input())
plans = input().split()
x,y = 1,1

for plan in plans:
    if plan == 'L':
       if x>1:
          x -= 1
    elif plan == 'R':
       if x<n:
          x += 1
    elif plan == 'U':
       if y>1:
          y -= 1
    elif plan == 'D':
       if y<n:
          y += 1

print(y,x)