def solution(s):
    answer = []
    count = 0
    zero_count = 0
    
    while s != '1':
        s_len = 0
        zero_count += s.count('0')
        s = s.replace('0',"")
        s_len = len(s)
        s = bin(s_len)[2:]
        count += 1
    
    answer.append(count)
    answer.append(zero_count)
    
        
    return answer