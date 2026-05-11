def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}

    for num in dice:
        counts[num] = counts.get(num, 0) + 1

    # 나온 숫자들을 등장 횟수 기준으로 정렬
    items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # 4개 모두 같음
    if len(counts) == 1:
        p = items[0][0]
        return 1111 * p

    # 3개 같고 1개 다름
    if len(counts) == 2 and items[0][1] == 3:
        p = items[0][0]
        q = items[1][0]
        return (10 * p + q) ** 2

    # 2개씩 같음
    if len(counts) == 2 and items[0][1] == 2:
        p = items[0][0]
        q = items[1][0]
        return (p + q) * abs(p - q)

    # 2개만 같고 나머지 2개는 다름
    if len(counts) == 3:
        result = 1
        for num, cnt in counts.items():
            if cnt == 1:
                result *= num
        return result

    # 모두 다름
    return min(dice)