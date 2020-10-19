total = [1, 4, 7, 2, 5, 8, 0, 3, 6, 9]
leftnum = ['1', '4', '7', '*']
middlenum = ['2', '5', '8', '0']
rightnum = ['3', '6', '9', '#']
leftfinger = "*"
rightfinger = "#"
result = ""


def solution(numbers, hand):
    global result, leftfinger, rightfinger
    for i in numbers:
        if total.index(i) <= 2:
            results("left", i)
        elif total.index(i) >= 7:
            results("right", i)
        else:
            vs = oper(i)
            if vs < 0:
                results("left", i)
            elif vs > 0:
                results("right", i)
            else:
                if hand == "right":
                    results("right", i)
                else:
                    results("left", i)
    return result


def oper(i):
    try:
        left = minor(middlenum.index(str(i)), leftnum.index(leftfinger))
    except:
        left = minor(middlenum.index(str(i)), middlenum.index(leftfinger))-1

    try:
        right = minor(middlenum.index(str(i)), rightnum.index(rightfinger))
    except:
        right = minor(middlenum.index(str(i)), middlenum.index(rightfinger))-1
    return left - right


def minor(i, j):
    if i >= j:
        return i - j
    else:
        return j - i


def results(dir, i):
    global result, leftfinger, rightfinger
    if dir == 'left':
        result += "L"
        leftfinger = str(i)
    else:
        result += "R"
        rightfinger = str(i)


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	, "left")
