def solution(s):
    p, y = 0, 0
    ans = True
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1
    
    if p != y:
        ans = False

    return ans