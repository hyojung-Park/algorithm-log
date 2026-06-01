def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c
        num = sorted(array[i-1:j])[k-1]
        answer.append(num)
        
    return answer

'''
    return [
        sorted(array[i-1:j])[k-1]
        for i, j, k in commands
    ]
'''