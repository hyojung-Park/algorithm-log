def cal(a, b):
    if a == True:
        return True
    if a == False and b == True:
        return True
    return False

def solution(x1, x2, x3, x4):
    x = cal(x1, x2)
    y = cal(x3, x4)
    
    if x == True and y == True:
        return True
    return False