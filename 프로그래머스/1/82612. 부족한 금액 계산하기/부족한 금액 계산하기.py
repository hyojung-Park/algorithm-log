def solution(price, money, count):
    fee = 0
    for c in range(1, count+1):
        fee += c * price
    ans = money - fee
        
    return -ans if ans < 0 else 0