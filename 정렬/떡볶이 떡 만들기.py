N,M = map(int,input().split())

array = list(map(int,input().split())) # 개별 떡의 길이

def binary_search(array,target,start,end):
    sum = 0 # 절단값들을 더하는 변수

    if start >= end:
        return None

    mid = (start+end) // 2 # 현재 절단점

    for i in array:
        if (i-mid) >= 0: # 음수를 더하지 않기 위해
            sum += i-mid
        else:
            continue

    if target == sum: # 절단값이 정확할때
        return mid

    elif target > sum: # 잘라서 모은 떡의 길이의 합이 타겟값보다 모자랄때
        return  binary_search(array,target,start,mid-1)

    else: #
        return  binary_search(array,target,mid+1,end)

start = 0
end = max(array) #제일 큰 떡의 길이를 초기 end 값으로 설정한다

result = binary_search(array,M,start,end)
# 최적의 절단값 구함

print(result)
