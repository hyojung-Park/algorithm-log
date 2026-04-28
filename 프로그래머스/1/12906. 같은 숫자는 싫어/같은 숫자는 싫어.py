def solution(arr):
    ans = [arr[0]] # 첫 인덱스는 그냥 넣어둠
    idx = 1 # 기준인덱스 지정
    
    for i in range(idx, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
            idx = i + 1
        
    return ans