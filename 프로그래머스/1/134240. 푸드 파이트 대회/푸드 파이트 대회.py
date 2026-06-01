def solution(food):
    '''
    음식개수 // 2 만큼 인덱스를 붙이고, 마지막 인덱스까지 끝나면 0 을 붙인 뒤, 앞을 뒤집은 문자열을 붙임
    '''
    left = ''
    
    for i in range(1, len(food)):
        left += (food[i] // 2) * str(i)
    
    answer = left + '0' + left[::-1]
    
    return answer