from collections import deque

def solution(people, limit):
    answer = 0
    people.sort() # 오름차순 정렬
    dq = deque(people)
    
    while dq:
        right = dq.pop()
        if not dq:
            answer += 1
            break
        left = dq[0]
        
        if right + left <= limit:
            dq.popleft()
        answer += 1
        
    return answer