import copy


def solution(n, lost, reserve):
    lost2 = copy.deepcopy(lost)
    reserve2 = copy.deepcopy(reserve)

    for i in lost:
        if i in reserve:
            lost2.remove(i)
            reserve2.remove(i)
        elif i-1 in reserve2:  # and i+1 not in reserve:
            lost2.remove(i)
            reserve2.remove(i-1)
        elif i+1 in reserve2:  # and i-1 not in reserve:
            lost2.remove(i)
            reserve2.remove(i+1)
    print(n-len(lost2))
    return n-len(lost2)


solution(10, [3, 9, 10], [3, 8, 9])
