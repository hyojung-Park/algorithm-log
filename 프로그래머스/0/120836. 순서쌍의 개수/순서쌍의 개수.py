def solution(n):
    cnt = 0
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                cnt += 1 # (4, 4)
            else:
                cnt += 2 # (1, 3), (3, 1) 한쌍
                
    return cnt