def solution(s, n):
    '''
    A 65 
    Z 90
    a 97
    z 122
    ' ' 32
    '''
    answer = ''

    # 91 ~ 96 / 123~ 라면 -26
    for i in s:
        o = ord(i)
        
        if 65 <= o <= 90 and 91 <= o + n:
            answer += chr(o + n - 26)
        elif 97 <= o and o + n > 122:
            answer += chr(o + n - 26)
        elif o == 32:
            answer += ' '
        else:
            answer += chr(o + n)
            
    return answer