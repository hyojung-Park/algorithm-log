def solution(s):
    ls = list(s)
    
    for j in range(len(s)):
        for i in range(len(s)-1):
            if ls[i] < ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i] 
    
    return ''.join(ls)