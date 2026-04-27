def solution(left, right):
    arr = [i for i in range(left, right+1)]
    ls = []
    
    # 1. 약수의 개수 구하기
    for num in range(left, right+1):
        cnt = 0
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
        ls.append(cnt)
    
    # 2. 짝수라면 더하고 홀수라면 뺴기
    ans = 0
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            ans += arr[i]
        else:
            ans -= arr[i]
    
    return ans