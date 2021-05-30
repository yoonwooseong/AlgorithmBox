result = []

def solution(numbers):
    adds(numbers)
    return sorted(list(set(result)))

def adds(numlist):
    if len(numlist) == 1:
        return 0
    else:
        for i in numlist[1:]:
            result.append(numlist[0] + i)
    adds(numlist[1:])

solution([5,0,2,7])