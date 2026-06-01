def solution(a, b, n):
    answer = 0
    while a <= n:
        # 가져다줄 개수
        tmp = n // a
        take = tmp * a
        # 가져다주고 남은 병의 수
        n = n - take
        # 새로 받아오는 병의 수 
        new = tmp * b
        # 받아 오고 남은 병의 수
        n += new
        answer += new
    
    return answer