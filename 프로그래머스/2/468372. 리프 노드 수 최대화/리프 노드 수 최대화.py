def f(n, d, s, split):
    if d == 0:
        return n
    
    dis = min(n, d)
    leaf = n - dis
    
    two = leaf if s*2 > split else leaf + f(dis*2, d-dis, s*2, split)
    three = leaf if s*3 > split else leaf + f(dis*3, d-dis, s*3, split)
    
    if two == leaf and three == leaf:
        return n
    
    return max(two, three)

def solution(dist_limit, split_limit):
    answer = f(1, dist_limit, 1, split_limit)
    
    return answer