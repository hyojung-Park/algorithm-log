def solution(my_string, m, c):
    s_li = []
    answer = ''
    
    for i in range(0, len(my_string), m):
        s_li.append(my_string[i:i+m])
    
    for s in s_li:
        answer += s[c-1]
    
    return answer