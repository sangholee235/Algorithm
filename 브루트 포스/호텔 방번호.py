while 1:
    try:
        count = 0
        # 수의 범위 입력 받기
        a, b = map(int, input().split())
        # 0~9 까지 초기화
        num = [0 for i in range(10)]

        for i in range(a, b + 1):
            # 4자리수
            if i >= 1000:
                num[i // 1000] += 1
                num[(i % 1000) // 100] += 1
                num[(i % 100) // 10] += 1
                num[i % 10] += 1

            # 3자리수
            elif i >= 100:
                num[(i % 1000) // 100] += 1
                num[(i % 100) // 10] += 1
                num[i % 10] += 1

            # 2자리수 미만
            else:
                num[(i % 100) // 10] += 1
                num[i % 10] += 1

            # 2번 이상 등장하지 않았다면
            if max(num) < 2:
                # 카운트++
                count += 1
                
            # 저장 리스트 초기화
            num = [0 for i in range(10)]

        print(count)
    # 예외처리
    except:
        break