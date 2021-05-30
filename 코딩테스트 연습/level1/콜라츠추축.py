def solution(num):
    for i in range(500):
        if num % 2 == 0:
            num /= 2
        elif num == 1:
            return i
        else:
            num = (num * 3 + 1)
    return -1


solution(6)
