def solution(a):
    lists = list(set(a))
    resultcount = []
    count = 0
    print(lists)

    for i in lists:
        resultcount.append(a.count(i))

    if max(resultcount) % 2 == 0:
        result = max(resultcount)
    else:
        result = max(resultcount)-1
    print(resultcount)
    for i in resultcount:
        if result == i:
            count += 1
    print(result * count * 2)
    return result * count * 2


solution([0])
