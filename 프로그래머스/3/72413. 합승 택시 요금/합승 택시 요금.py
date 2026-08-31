'''
어디서 갈라져야하지?
최적의 경로를 선택하다가, 도착할 수 있는 사람이 있다면 일단 보내줘야 함.
[로직1 - 실패]
1. for문 안에서 한명이라도 도착지를 만났다면, 그자리에서 가중치만큼만 answer에 추가
2. 남은 사람은 마저 진행해서 도착한만큼을 answer에 추가? 

[로직2]
1. s-합승지점 + a-합승지점 + b-합승지점
2. 전부 돌려서 dist[k]의 합이 가장 작은 경우를 찾으면 된다
'''

import heapq

def dijkstra(start, n , graph):
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, ((0, start)))
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dist[cur_node]:
            continue
        
        for neighbor, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return dist
    
# 노드 수 n, 출발 지점 s, A 도착지점 a, B 도착지점 b, 택시요금 fares (c지점, d지점, f요금)
def solution(n, s, a, b, fares):
    answer = float('inf')
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    A = dijkstra(a, n, graph)
    B = dijkstra(b, n, graph)
    st = dijkstra(s, n, graph)
    
    for i in range(1, n+1):
        fare = A[i] + B[i] + st[i]
        
        if fare < answer:
            answer = fare
            
    return answer