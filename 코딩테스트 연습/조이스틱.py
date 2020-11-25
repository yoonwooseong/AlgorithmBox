def solution(name):
    result = 0
    stack = list(name)

    for i in range(len(name)):
        sor = stack.pop()
        if ord(sor) - 65 >= 13:
            result += 91 - ord(sor)
        else:
            result += ord(sor) - 65
    idx = 0
    print(result)
    stack2 = list(name)
    while True:
        stack2.pop()
        if len(stack2) == 1:
            break
        left = 1
        right = 1
        for i in range(len(name)):
            if name[idx-left] != "A":
                break
            else:
                left += 1
            if name[idx+right] != "A":
                break
            else:
                right += 1
        if left < right:
            result += left
        else:
            result += right
        idx += 1
        print(left, right)
    print(result)
    return result


# JANAAAAN
solution("JEROEN")
# A기준 빼가지고 위로 갈지 아래로 갈지
# A갯수에 따라 오른쪽 갈지 왼쪽 갈지
'''
def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
'''
