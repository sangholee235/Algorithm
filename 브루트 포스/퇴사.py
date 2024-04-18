# 퇴사까지 남은 날짜
n = int(input())

# 작업리스트 선언

work = [[]*2 for _ in range(n)]

for i in work:
    t,p = map(int,input().split())

    i.append(t)
    i.append(p)
