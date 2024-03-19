def solution(x):
    answer = True
    
    x_list = [int(digit) for digit in str(x)]
    
    x_sum = sum(x_list)
    
    if x % x_sum != 0:
        answer = False
        
    return answer