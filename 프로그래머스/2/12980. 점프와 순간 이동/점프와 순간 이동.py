'''
뒤에서부터 센다
짝수일땐 순간이동
홀수일땐 점프
'''
def solution(n):
    ans = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
    
    return ans