def solution(a, d, included):
    ls = [a]
    for i in range(1, len(included)):
        ls.append(ls[i-1] + d)
    
    ans = 0
    for i in range(len(included)):
        if included[i]:
            ans += ls[i]
    
    return ans
    
    