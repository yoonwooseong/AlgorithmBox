def solution(n, delivery):
    result = []
    result_str = ""

    for i in range(n):
        result.append("?")
    sort_delivery = sorted(delivery, key=lambda x: -x[2])

    for i in sort_delivery:
        if i[2] == 1:
            result[i[0]-1] = "O"
            result[i[1]-1] = "O"
        else:
            if result[i[0]-1] == "O":
                result[i[1]-1] = "X"
            elif result[i[1]-1] == "O":
                result[i[0]-1] = "X"

    for i in result:
        result_str += i
    print(result_str)


solution(7,	[[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]])
# 모두 ? 시작 인덱스2이 1일때 0,1 인덱스 값들 o로변환
# 인덱스2 가 0일때 해당 인덱스 중 o가 있으면 x
