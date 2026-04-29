def solution(my_string, letter):
    ls = [i for i in list(my_string) if i != letter]
    return ''.join(ls)