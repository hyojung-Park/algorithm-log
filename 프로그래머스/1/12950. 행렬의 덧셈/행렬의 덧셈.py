def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        ls = []
        for j in range(len(arr1[0])):
            ls.append(arr1[i][j] + arr2[i][j])
        ans.append(ls)
    
    return ans