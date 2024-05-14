T = int(input())

for tc in range(1, T + 1):
    bit = input()
    answer = 0
    code = 1  # 초기 코드를 문자열 '0'으로 설정

    for i in range(len(bit)):
        if bit[i] == "1" and code == "0":  # 문자열 '1'과 비교
            answer += 1
            code = "1"
        elif bit[i] == "0" and code == "1":  # 문자열 '0'과 비교
            answer += 1
            code = "0"

    print("#" + str(tc) + " " + str(answer))

## 결론 문자열로 받고 접근하자
