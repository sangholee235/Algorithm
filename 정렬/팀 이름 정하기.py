name = list(map(str,input().split()))

n = int(input())

word_list = []

for i in range(1,n):
    word_list = list(map(str,input().split()))


for i in name:
    check = []

    for j in range(len(word_list)):
        check[i] = word_list[j].count(i)

    