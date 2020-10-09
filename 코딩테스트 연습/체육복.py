def solution(n, lost, reserve):
    reserve_2 = set(reserve)-set(lost)
    lost_2 = set(lost)-set(reserve)

    for i in reserve_2:
        if i-1 in lost_2:
            lost_2.remove(i-1)
        elif i+1 in lost_2:
            lost_2.remove(i+1)

    return n-len(lost_2)
