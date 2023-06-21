array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 1부터 배열 끝까지 i가 이동한다
    for j in range(i,0,-1): # i번째부터 배열의 시작 까지 뒤로 이동한다
        if array[j] < array[j-1]: # 뒤에 있는게 앞에 있는 값보다 작을때 (비정렬상태)
            array[j],array[j-1] = array[j-1],array[j] # 스와핑
        else: # 본인보다 작은 데이터를 만났을때
            break






