def solution(array, commands):
    answer = []
    
    for c in commands:
        arr = array[::]
        k = sorted(arr[c[0]-1:c[1]])[c[2]-1]
        answer.append(k)
        
    return answer