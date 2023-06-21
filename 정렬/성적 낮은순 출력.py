n = int(input())

array = []

for i in range(n):
    input_data = input().split() # 쪼개서 입력 받기
    array.append(input_data[0],int(input_data[1]))
    