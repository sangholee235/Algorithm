array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end: # 원소가 1개 남으면 종료
        return
    pivot = start # 첫번째 원소를 피벗으로 한다
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            # 피벗보다 큰 데이터 찾을때 까지
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -=1

        if left > right: # 엇갈렸다면 작은 데이터와 피벗 교체
            array[right] , array[pivot] = array[pivot], array[right]

        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체한다
            array[left] , array[right] = array[right] , array[left]

    quick_sort(array,start,right-1) # 왼쪽 부분 정렬
    quick_sort(array,right+1,end) # 오른쪽 부분 정렬

quick_sort(array,0,len(array)-1)

print(array)


