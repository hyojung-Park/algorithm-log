def solution(st):
    
    stack = []
    
    for s in st:
        if s == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True