from collections import deque

test = int(input())

for _ in range(test):
    # 문서의 개수, 타겟 문서 위치 입력 받기
    a,b = map(int,input().split())

    # 큐 입력받기 
    queue = deque(map(int,input().split()))
    # 큐[인덱스번호][우선순위]
    queue = deque([(index, i) for index, i in enumerate(queue)])

    count = 0

    while True:
        # 큐의 맨앞이 큐에서 우선순위가 가장 크다면?
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            count += 1 # 카운트 ++
            # 그 큐의 인덱스가 찾던 문서의 인덱스라면? 카운트 출력하고 종료
            if queue[0][0] == b:
                print(count)
                break
            else: # 아니라면 맨왼쪽 팝하고 계속 진행
               queue.popleft()
        # 최대값이 아닌 경우? 다시 큐에 추가 삽입됨
        else:
            queue.append(queue.popleft())
