def solution(s):
    arr = s.split(' ')
    new_arr = []
    
    for w in arr:
        if w == '':
            new_arr.append('')
        
        else:
            new_w = w[0].upper() + w[1:].lower()
            new_arr.append(new_w)
    
    return ' '.join(new_arr)