def solution(s):
    lis = s.split()
    n_li = []
    
    for i in range(len(lis)):
        if lis[i] == 'Z':
            n_li.append(-int(n_li[i-1]))
        else:
            n_li.append(int(lis[i]))
    
    return sum(n_li)