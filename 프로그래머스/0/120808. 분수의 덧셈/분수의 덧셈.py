import math

def solution(numer1, denom1, numer2, denom2):
    n3 = numer1*denom2 + numer2*denom1
    d3 = denom1*denom2
    
    gcd = math.gcd(n3, d3)
    answer = [n3/gcd, d3/gcd]
    
    return answer