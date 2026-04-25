def solution(id_list, report, k):
    # 1. d1 = { "신고자" : [신고대상1, 신고대상2]} 생성
    
    # 신고 중복제거 
    report = set(report)
    d1 = {}
    
    for name in id_list:
        d1[name] = []
    
    for r in report:
        reporter, reported = r.split()
        d1[reporter].append(reported)
        
        
    # 2. d2 = { "신고대상1" : 신고횟수 } 생성
    d2 = {}
    
    for name in id_list:
        d2[name] = 0
        
        for reporter, reported in d1.items():
            if name in reported:
                d2[name] += 1
    
    
    # 3. 신고횟수가 k가 넘는 신고대상 리스트 생성
    reported = []
    for name, cnt in d2.items():
        if cnt >= k:
            reported.append(name)
    
    
    # 4. d1의 value에 신고 대상이 몇 명 포함되어 있는 지 계산 
    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        cnt = 0
        for n in reported:
            if n in d1[id_list[i]]:
                cnt += 1
        answer[i] = cnt
    
    return answer

