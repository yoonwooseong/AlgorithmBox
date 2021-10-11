def solution(numbers, target):
    count = 0
    li = [0]
    li2 = []
    for num in numbers:
        if len(li) != 0:
            for i in plusOrMin(li, num):
                li2.append(i)
            li.clear()
        else:
            for i in plusOrMin(li2, num):
                li.append(i)
            li2.clear()

    if len(li) == 0:
        for i in li2:
            if target == i:
                count += 1
    else:
        for i in li:
            if target == i:
                count += 1

    return count


def plusOrMin(res, num):
    lis = []
    for resone in res:
        lis.append(resone+num)
        lis.append(resone-num)
    return lis


solution([1, 1, 1, 1, 1], 3)
