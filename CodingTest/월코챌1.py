def solution(a, b):
    result = []
    for i in zip(a, b):
        result.append(i[0]*i[1])
    return sum(result)


solution([1, 2, 3, 4], [-3, -1, 0, 2])
