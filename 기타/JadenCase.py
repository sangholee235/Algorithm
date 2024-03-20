def solution(s):
    answer = ''
    capitalize_next = True  # 다음 문자를 대문자로 변환할지 여부를 나타내는 플래그
    
    for char in s:
        # 현재 문자가 공백인 경우 다음 문자를 대문자로 변환해야 함
        if char == ' ':
            capitalize_next = True
            answer += char
        # capitalize_next 플래그가 True이면 현재 문자를 대문자로 변환하고 플래그를 False로 변경
        elif capitalize_next:
            answer += char.upper()
            capitalize_next = False
        # capitalize_next 플래그가 False이면 현재 문자를 소문자로 변환
        else:
            answer += char.lower()
    
    return answer