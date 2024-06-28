T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리한다
for test_case in range(1, T + 1):

    # 날짜개수 입력 받기
    N = int(input())

    # 날짜별 가격 리스트 입력 받기
    num_list = list(map(int, input().split()))

    # 최대값 밸류 저장
    max_value = max(num_list)

    # 구매할 상품 가격 리스트 초기화
    buy_list = []

    money = 0

    for i in range(len(num_list)):
        # 앞에서 부터 빼고 삭제
        val = num_list.pop(0)
        # 현재 값이 최댓값이라면
        if val == max_value:
            if len(buy_list) == 0:  # 구매 리스트가 비어있으면
                continue
            else:  # 비어있지 않다면
                # 구매했던 리스트에서
                for j in range(len(buy_list)):
                    buy_val = buy_list.pop(0)
                    # 최대값에 팔아서 차익 챙긴 값 저장
                    money = money + max_value - buy_val
            # 지금 있는 리스트에서 최댓값 초기화
            if len(num_list) != 0:
                max_value = max(num_list)
        else:
            # 최대값이 아니니까 살 리스트에 추가함
            buy_list.append(val)

    print("#{} {}".format(test_case, money))
