'''
모든 쌍 비교시 터짐
def solution(phone_book):
    dict = {}
    for num in phone_book:
        for n in dict:
            if num.startswith(n) or n.startswith(num):
                dict[n] += 1

            if dict[n] >= 1:
                return False
            
        dict[num] = 0
    
    return True
'''
def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    return True