def solution(genres, plays):
    # 1. 재생수 높은 순서대로 장르 정리
    # 1-1. {장르 : 재생수} 딕셔너리 d1 생성해서 더 높은 수로 재생수 갱신
    # 1-2. sorted()로 정렬 후 재생수 높은 순서대로 장르 명을 담은 list 생성
    
    d1 = {}

    for i in range(len(genres)):
        d1[genres[i]] = d1.get(genres[i], 0) + plays[i]
    
    d2 = sorted(d1.items(), key= lambda x : x[1], reverse = True)
    names = [x[0] for x in d2]
            
    
    # 2. 재생수 높은 장르에서 많이 재생된 노래 2개 뽑기 
    # d3 = {장르명 : [(재생수, 고유번호), ...]}
    '''
        {
            "classic" : [(500, 0), (150, 2), (800, 3)]
        }
    '''
    d3 = {}
    for g in set(genres):
        d3[g] = []
    
    for i in range(len(genres)):
        d3[genres[i]].append((plays[i], i))
    
    answer = []
    
    # 장르 명 list 돌면서 pop이라면 d3["pop"]을 뽑아 재생횟수로 정렬 + 재생횟수가 같다면 고유번호 낮은 순 정렬
    for n in names:
        ls = d3[n]
        ls.sort(key = lambda x : (-x[0], x[1]))
        
        cnt = 0
        for i in range(len(ls)):
            answer.append(ls[i][1])
            cnt += 1
            if cnt == 2:
                break
        
    return answer