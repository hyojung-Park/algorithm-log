def solution(num_list, n):
    ans = []
    idx = 0
    while (idx < len(num_list)):
        ans.append([num_list[i] for i in range(idx, idx + n)])
        idx += n
            
    return ans