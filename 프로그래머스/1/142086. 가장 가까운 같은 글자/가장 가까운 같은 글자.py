def solution(s):
    answer = [-1]
    
    # 1. 앞에서부터 한 문자씩 확인
    for i in range(1, len(s)):
        flag = -1
        # 2. 자신의 바로 앞 인덱스부터 앞으로 가면서 확인
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                flag = i-j
                break
        if flag != -1:
            answer.append(i-j)
        else:
            answer.append(-1)
        
    return answer