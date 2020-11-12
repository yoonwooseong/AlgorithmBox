def solution(a, b):
    result = 0
    for i in zip(a, b):
        result += i[0]*i[1]

    return result


solution([1, 2, 3, 4], [-3, -1, 0, 2])
