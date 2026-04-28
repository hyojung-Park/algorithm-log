def solution(s):
    num = set(str(i) for i in range(0, 10))

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in num:
                return False
    else:
        return False        

    return True