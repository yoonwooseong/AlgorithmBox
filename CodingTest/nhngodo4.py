def solution(cardNumber):
    stack = list(str(cardNumber))
    resultnum = 0
    if len(str(cardNumber)) % 2 == 0:
        for i in range(0, len(str(cardNumber)), 2):
            stack[i] = str(2*int(stack[i]))
    else:
        for i in range(1, len(str(cardNumber)), 2):
            stack[i] = str(2*int(stack[i]))

    for i in stack:
        if len(i) > 1:
            stack.remove(i)
            stack.append(i[0])
            stack.append(i[1])

    for i in stack:
        resultnum += int(i)

    if resultnum % 10 == 0:
        return "VALID"
    else:
        return "INVALID"


solution("21378")
