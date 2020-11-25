def solution(name):
    result = len(name)-1
    stack = list(name)

    for i in range(len(name)):
        sor = stack.pop()
        if sor == 'A':
            result -= 1

        if ord(sor) - 65 >= 13:
            result += 91 - ord(sor)
        else:
            result += ord(sor) - 65
    return result


# JANAAAAN
solution("JAN")
# A기준 빼가지고 위로 갈지 아래로 갈지
# A갯수에 따라 오른쪽 갈지 왼쪽 갈지
