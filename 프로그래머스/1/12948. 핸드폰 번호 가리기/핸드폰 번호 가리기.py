def solution(phone_number):
    idx = len(phone_number) - 4
    front = '*' * idx
    back = phone_number[idx:]
    return front + back