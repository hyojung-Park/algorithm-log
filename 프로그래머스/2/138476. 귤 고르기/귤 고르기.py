def solution(k, tangerine):
    counts = {}
    
    for t in tangerine:
        counts[t] = counts.get(t, 0) + 1
    
    li = sorted(counts.values(), reverse = True)
    
    cnt = 0 # 담은 귤의 수
    answer = 0 # 종류 수
    
    for i in li:
        cnt += i # 담고
        answer += 1 # 종류수 카운트
        if cnt >= k: # k보다 많아지면 중단
            break
    
    return answer