from collections import deque

def diff_count(a, b):
    # a와 b가 몇 글자 다른 지 세서 리턴
    cnt = 0
    for i, j in zip(a,b):
        if i != j:
            cnt += 1
    return cnt
                    
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    dq = deque([[begin, 0]])
    
    while dq:
        node = dq.popleft()
        if node[0] == target:
            return node[1]
        
        for w in words:
            if w not in visited and diff_count(node[0], w) == 1:
                dq.append([w, node[1] + 1])
                visited.add(w)
                