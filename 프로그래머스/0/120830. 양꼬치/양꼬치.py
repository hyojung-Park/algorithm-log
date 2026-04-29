def solution(n, k):
    ans = 12000 * n + 2000 * k
    free = 0
    
    if n >= 10:
        free += n // 10
    
    return ans - free * 2000