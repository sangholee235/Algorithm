def solution(array, commands):
    answer = []
    
    # 커맨드 길이 만큼 반복
    for i in range(len(commands)):
        start_idx = commands[i][0] - 1  # 시작 인덱스 (1 빼기)
        end_idx = commands[i][1]  # 종료 인덱스
        selected_idx = commands[i][2] - 1  # 선택 인덱스 (1 빼기)

        # 배열 슬라이싱 후 정렬
        selected_slice = sorted(array[start_idx:end_idx])
        
        # 선택된 인덱스의 값 추가
        answer.append(selected_slice[selected_idx])
        
    return answer
