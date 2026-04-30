def solution(emergency):
    sorted_em = sorted(emergency, reverse = True)
    answer = []
    
    for n in emergency:
        answer.append(sorted_em.index(n) + 1)
    return answer