def solution(n):
    lst = [i for i in range(1, n+1)]
    ans = []
    for i in lst:
        if i % 2 != 0:
            ans.append(i)
            
    return ans