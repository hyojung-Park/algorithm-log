def solution(arr, divisor):
    ans = [n for n in arr if not n % divisor]
    ans.sort()
    
    if not ans:
        return [-1]
    
    return ans