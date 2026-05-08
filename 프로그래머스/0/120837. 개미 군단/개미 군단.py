def solution(hp):
    
    cnt = 0    
    
    if hp >= 5:
        cnt = cnt + hp // 5
        hp = hp % 5
    if hp >= 3:
        cnt = cnt + hp // 3
        hp = hp % 3
    if hp >= 1:
        cnt = cnt + hp // 1
        hp = 0
        

    return cnt