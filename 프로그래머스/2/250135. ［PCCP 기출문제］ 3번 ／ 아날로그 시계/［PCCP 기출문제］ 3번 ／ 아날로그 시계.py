def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    M = 43200  # 360도 * 120, 소수 방지용 단위

    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    if start % 43200 == 0:
        answer += 1

    for t in range(start, end):
        s_cur = (t * 720) % M
        m_cur = (t * 12) % M
        h_cur = t % M

        s_next = ((t + 1) * 720) % M
        m_next = ((t + 1) * 12) % M
        h_next = (t + 1) % M

        cur_m = (m_cur - s_cur) % M
        next_m = (m_next - s_next) % M

        cur_h = (h_cur - s_cur) % M
        next_h = (h_next - s_next) % M

        if cur_m > 0 and (next_m > cur_m or next_m == 0):
            answer += 1

        if cur_h > 0 and (next_h > cur_h or next_h == 0):
            answer += 1

        if (t + 1) % 43200 == 0:
            answer -= 1

    return answer