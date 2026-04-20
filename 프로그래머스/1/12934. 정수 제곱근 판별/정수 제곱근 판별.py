import math

def solution(n):
    n2 = math.sqrt(n)
    if int(n2) == n2:
        return (n2+1)**2
    else:
        return -1
