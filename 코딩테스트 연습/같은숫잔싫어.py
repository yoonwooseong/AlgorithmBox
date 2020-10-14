def solution(arr):
    num = 10
    arr2 = []
    for i in arr:
        if i != num:
            arr2.append(i)
        num = i
    return arr2
    print(arr2)


solution([1,1,3,3,0,1,1])


