def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_s = 0
    two_s = 0
    three_s = 0
    
    for i in range(len(answers)):
        ans = answers[i]
        # 1번
        if one[i % len(one)] == ans:
            one_s += 1
        
        # 2번
        if two[i % len(two)] == ans:
            two_s += 1

        # 3번
        if three[i % len(three)] == ans:
            three_s += 1
    
    score = max(one_s, two_s, three_s)
    answer = []
    
    if one_s == score:
        answer.append(1)
    if two_s == score:
        answer.append(2)
    if three_s == score:
        answer.append(3)
        
    return answer