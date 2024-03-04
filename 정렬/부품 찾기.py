N = int(input())
item = list(map(int,input().split()))
item.sort() # 오름차순으로 정렬

M = int(input())
x = list(map(int,input().split()))


def binary_search(item,target,start,end):
    if start > end:
        return None
    mid = (start+end) // 2

    if item[mid] == target:
        return mid

    elif item[mid] > target:
        return binary_search(item,target,start,mid-1)

    else:
        return binary_search(item,target,mid+1,end)

for i in x:

    result = binary_search(item,i,0,N-1)

    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')



