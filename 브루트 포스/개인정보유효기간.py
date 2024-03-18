def solution(today, terms, privacies):
    
    d = {}
    answer = []
    today_lst = list(map(int,today.split('.'))) # 오늘 날짜 리스트로 변환
    
    for term in terms:
        n, m = term.split()
        d[n] = int(m) * 28
    
    for i in range(len(privacies)):
        date,s = privacies[i].split()
        date_lst = list(map(int,date.split('.')))
        year = (today_lst[0] - date_lst[0]) * 336
        month = (today_lst[1] - date_lst[1]) * 28
        day = today_lst[2] - date_lst[2]
        total = year + month + day
        if d[s] <= total:
            answer.append(i+1)
        
    
    return answer