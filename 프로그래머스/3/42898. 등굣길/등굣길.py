def solution(m, n, puddles):
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    
    for i, j in puddles:
        map[j-1][i-1] = -1
    
    for i in range(m):
        if map[0][i] == -1:
            break
        map[0][i] = 1
    
    for j in range(n):
        if map[j][0] == -1:
            break
        map[j][0] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if map[i][j] == -1:
                continue
            
            left = map[i-1][j]
            top = map[i][j-1]
            
            if left != -1:
                map[i][j] += left
            
            if top != -1:
                map[i][j] += top
            
            map[i][j] %= 1000000007
    
    return map[n-1][m-1]