def solution(clothes):
    d = {}
    
    for name, tp in clothes:
        d[tp] = d.get(tp, 0) + 1
        
    ans = 1
    
    for cnt in d.values():
        ans *= cnt + 1

    return ans - 1  