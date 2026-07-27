def solution(n, times):
    times.sort()
    left = 1
    right = times[-1] * n
    
    while left < right:
        mid = (left+right) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t
        
        if cnt >= n:
            right = mid 
        else:
            left = mid + 1
    
    return left