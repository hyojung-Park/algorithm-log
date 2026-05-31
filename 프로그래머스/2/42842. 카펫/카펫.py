def solution(brown, yellow):
    
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow):
        j = yellow / i
        if int(j) == j:
            a = i + 2
            b = j + 2
            if 2 * a + 2 * b - 4 == brown:
                return [b, a]