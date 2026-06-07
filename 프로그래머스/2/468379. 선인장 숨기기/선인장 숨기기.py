from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    rain = [[INF] * n for _ in range(m)]

    for time, (r, c) in enumerate(drops, start=1):
        rain[r][c] = time

    # 1. 각 행마다 가로 w칸 최솟값
    # 각 행마다 n-w+1개의 최솟값이 나옴
    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for r in range(m):
        dq = deque() # 현재 행에서 최솟값 후보의 열 번호를 저장할 덱

        for c in range(n): # 현재 행 왼쪽부터 확인
            while dq and rain[r][dq[-1]] >= rain[r][c]:
                # 현재 값보다 크거나 같은 기존 후보는
                # 앞으로 최솟값이 될 수 없으므로 제거
                dq.pop()
                
            # 현재 열 번호를 최솟값 후보로 추가
            dq.append(c)
            
            # 현재 창문범위보다 왼쪽에 있는 후보 제거
            if dq[0] <= c - w:
                dq.popleft()
                
            # 창문 길이가 w가 된 순간부터 최솟값 기록 시작
            if c >= w - 1:
                # c-w+1은 현재 창문의 시작 열 번호
                # 그 위치에 현재 창문의 최솟값을 기록
                row_min[r][c - w + 1] = rain[r][dq[0]]

    # 2. 세로 h칸 최솟값
    # (r,c)를 좌상단으로 하는 h*w 직사각형의 최솟값을 저장
    area_min = [[0] * (n - w + 1) for _ in range(m - h + 1)]

    # 열을 돌면서 (n-w+1)까지 확인 
    for c in range(n - w + 1):
        # 현재 열에서 최솟값 후보의 행 번호 저장
        dq = deque()
        
        # 현재 열 c에 있는 row_min의 모든 행 확인
        for r in range(m):
            # 현재 값보다 크거나 같은 기존 후보를 뒤에서 제거
            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()
            
            # 현재 행 번호를 최솟값 후보로 추가
            dq.append(r)
            
            # 현재 창문 범위를 벗어난 후보 제거
            if dq[0] <= r - h:
                dq.popleft()

            # 세로 창문이 h만큼이 된 순간부터 기록
            if r >= h - 1:
                # 가장 위 좌표: r - h + 1
                top = r - h + 1
                # 현재 세로 창문의 최솟값을 저장
                area_min[top][c] = row_min[dq[0]][c]

    # 3. 행 우선 순회로 정답 선택
    best_time = 0
    answer = [0, 0]

    for r in range(m - h + 1):
        for c in range(n - w + 1):
            if area_min[r][c] > best_time:
                best_time = area_min[r][c]
                answer = [r, c]

    return answer                                                           