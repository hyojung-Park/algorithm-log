from collections import deque

def solution(numbers, direction):
    dq = deque(numbers)
    
    if direction == 'right':
        n = dq.pop()
        dq.appendleft(n)
    else:
        n = dq.popleft()
        dq.append(n)
    
    return list(dq)