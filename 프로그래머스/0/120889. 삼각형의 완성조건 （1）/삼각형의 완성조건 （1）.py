def solution(sides):
    a = max(sides)
    b = sum(sides) - a
    
    if a < b :
        return 1
    else:
        return 2