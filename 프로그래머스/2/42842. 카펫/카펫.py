def solution(brown, yellow):
    
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h

            carpet_w = w + 2
            carpet_h = h + 2

            if 2 * carpet_w + 2 * carpet_h - 4 == brown:
                return [carpet_w, carpet_h]