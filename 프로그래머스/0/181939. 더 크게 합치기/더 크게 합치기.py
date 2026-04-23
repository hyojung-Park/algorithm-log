def solution(a, b):
    n1 = str(a) + str(b)
    n2 = str(b) + str(a)
    
    if int(n1) >= int(n2):
        return int(n1)
    else:
        return int(n2)