def solution(num_list):
    a = 1
    b = 0
    
    for n in num_list:
        a *= n
        b += n
    
    if a < b**2:
        return 1
    return 0