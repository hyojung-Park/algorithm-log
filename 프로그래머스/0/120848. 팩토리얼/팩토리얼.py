def fac(i):
    num = 1
    for i in range(1, i+1):
        num *= i
    return num

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if fac(i) <= n:
            answer = i
        else:
            break
        
    return answer