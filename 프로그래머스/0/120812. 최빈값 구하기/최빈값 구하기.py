def solution(array):
    lst = [0] * (max(array) + 1)
    
    for i in array:
        lst[i] += 1
    
    m = max(lst)
    cnt = 0
    ans = 0
    
    for i in range(len(lst)):
        if lst[i] == m:
            cnt += 1
            ans = i
        if cnt > 1:
            return -1
        
    return ans

    