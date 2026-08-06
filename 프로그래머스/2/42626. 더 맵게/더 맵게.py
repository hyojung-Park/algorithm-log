from collections import deque

def solution(scoville, K):
    scoville.sort()
    
    if scoville[0] >= K:
        return 0
    
    dq = deque(scoville)
    a = dq.popleft()
    b = dq.popleft()
    mix = deque([a + b * 2])
    answer = 1
    
    while True:
        min = float('inf')
        if dq:
            if dq[0] <= min:
                min = dq[0]
        
        if mix:
            if mix[0] <= min:
                min = mix[0]
        
        if min >= K:
            break
        
        if len(dq) + len(mix) < 2:
            return -1
        
        # dq와 mix에 둘다 원소가 존재할 때 
        if mix and dq:
            first = 0 # 가장 맵지 않은 음식
            second = 0 # 두 번째로 맵지 않은 음식 
            
            # mix쪽 최솟값이 더 작을 때
            if mix[0] < dq[0]:
                first = mix[0]
                mix.popleft() 
                # mix에 값이 남아있다면
                if mix:
                    # mix쪽 최솟값이 더 작을 때
                    if mix[0] < dq[0]:
                        second = mix[0]
                        mix.popleft()
                    # dq쪽 최솟값이 더 작을 때
                    else:
                        second = dq[0]
                        dq.popleft()
                
                # mix가 비었다면
                else:
                    # dq[0]이 최소임
                    second = dq[0]
                    dq.popleft()
                
            # dq쪽 최솟값이 더 작을 때 
            else:
                first = dq[0]
                dq.popleft()
                # dp에 값이 남아있다면
                if dq:
                    # mix쪽 최솟값이 더 작을 때
                    if mix[0] < dq[0]:
                        second = mix[0]
                        mix.popleft()
                    # dq쪽 최솟값이 더 작을 때
                    else:
                        second = dq[0]
                        dq.popleft()
                    
                # dp가 비었다면
                else:
                    # mix[0]이 최소임
                    second = mix[0]
                    mix.popleft()
            
            mix.append(first + second * 2)
            answer += 1
    
        # mix만 존재할때
        elif mix and not dq:
            a = mix.popleft()
            b = mix.popleft()
            mix.append(a + b * 2)
            answer += 1
            
        # dq만 존재할때 
        elif dq and not mix:
            a = dq.popleft()
            b = dq.popleft()
            mix.append(a + b * 2)
            answer += 1
            
    return answer