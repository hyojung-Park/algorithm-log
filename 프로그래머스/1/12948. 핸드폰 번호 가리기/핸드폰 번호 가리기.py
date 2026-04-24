def solution(phone_number):
    idx = len(phone_number) - 4
    return '*' * idx + phone_number[idx:]