def solution(citations):
    answer = 0
    
    for i in range(len(citations) + 1):
        cnt = 0
        
        for c in citations:
            if c >= i:
                cnt += 1
        
        if cnt >= i:
            answer = i
        
    return answer