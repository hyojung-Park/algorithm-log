def solution(my_string):
    li = ['a', 'e', 'i', 'o', 'u']
    
    for a in li:
        my_string = my_string.replace(a, '')
        
    return my_string