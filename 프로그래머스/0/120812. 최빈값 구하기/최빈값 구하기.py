def solution(array):
    lst = [0] * (max(array) + 1)
    
    for i in array:
        lst[i] += 1
    
    m = max(lst)
    cnt = 0
    ans = 0
    
    for i in range(len(lst)):
        if lst[i] == m:
            cnt += 1
            ans = i
        if cnt > 1:
            return -1
        
    return ans

'''
count = {}

for x in array:
    count[x] = count.get(x, 0) + 1
    
max_count = max(count.values())

if list(count.values()).count(max_count) >= 2:
    retrun -1
    
for key, value in count.items():
    if value == max_count:
        return key
'''
    