def solution(dartResult):
    answer = 0
    
    score = 0
    
    for i in range(dartResult):
        if dartResult[i].isdigit():
           # 만약 현재 문자가 숫자인 경우에만 실행함
           if dartResult[i+1] == "S":
              score += int(dartResult[i]) ** 1
           elif dartResult[i+1] == "D":
              score += int(dartResult[i]) ** 2
           elif dartResult[i+1] == "T":
              score += int(dartResult[i]) ** 3
           
        
            
        
    
    return answer