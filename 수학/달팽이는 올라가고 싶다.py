up,down,tree = map(int, input().split())

day = (tree-down)/(up-down)
# tree - down 하는 이유는 정상에 올라가고 떨어지지 않기 위해서
# up - down == 하루에 올라가는 양
# 이렇게 안짜고 반복문 돌리면 시간 초과 걸림

# 정수로 나눠 떨어지면
if day == int(day):
   print(int(day))

# 그렇지 않다면 +1일을 해준다
else:
   print(int(day)+1)