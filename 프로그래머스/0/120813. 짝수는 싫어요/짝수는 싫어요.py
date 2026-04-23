def solution(n):
    lst = [i for i in range(1, n+1)]
    ans = []
    for i in lst:
        if i % 2 != 0:
            ans.append(i)
            
    return ans

'''
    return [x for x in range(n + 1) if x % 2]
    0이면 False, 1이면 True -> x%2 홀수
'''