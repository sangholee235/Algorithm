def solution(edges):
    answer = [0,0,0,0]
    
    # 그래프 정보 저장
    exchangeCnts = {}
    
    for a,b in edges:
        if not exchangeCnts.get(a):
            exchangeCnts[a] = [0,0]
        if not exchangeCnts.get(b):
            exchangeCnts[b] = [0,0]
            
        exchangeCnts[a][0] += 1
        exchangeCnts[b][1] += 1
        
    for key, exchangeCnt in exchangeCnts.items():
        if exchangeCnt[0] >= 2 and exchangeCnt[1] == 0:
            answer[0] = key
        elif exchangeCnt[0] == 0 and exchangeCnt[1] > 0:
            answer[2] += 1
        elif exchangeCnt[0] >= 2 and exchangeCnt[1] >= 2:
            answer[3] += 1

    # 모든 경우에서 2,3 경우를 빼면 1의 경우가 남음 
    answer[1] = (exchangeCnts[answer[0]][0] - answer[2] - answer[3])
        
        
    return answer