def solution(a, d, included):
    ans = 0
    
    for i in range(len(included)):
        if included[i]:
            ans += a + (d * i)
        
    return ans
    
    