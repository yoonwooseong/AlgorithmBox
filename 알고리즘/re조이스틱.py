def solution(name):
    idx, answer = 0, 0
    listname = []
    for i in name:
        listname.append(min(ord(i) - ord("A"), ord("Z")-ord(i)+1))
        print(listname)
    while True:
        print(listname, idx)
        answer += listname[idx]
        listname[idx] = 0
        if sum(listname) == 0:
            break
        left, right = 1, 1
        while listname[idx - left] == 0:
            left += 1
        while listname[idx - right] == 0:
            right += 1
        if left < right:
            answer += left
            idx += -left
        else:
            answer += right
            idx += right
    print(answer)
    return answer


solution("JEROEN")
