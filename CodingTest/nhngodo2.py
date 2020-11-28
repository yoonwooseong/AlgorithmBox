def solution(page, broken):
    result = ""
    count = 0
    if page == 100:
        return 0
    elif len(broken) == 10:
        if page > 100:
            return page - 100
        else:
            return 100 - page
    else:
        stack = list(str(page))

        for idx, i in enumerate(stack):
            if int(i) not in broken:
                print(i)
                result += i
            else:
                sumi = int(i)
                mini = int(i)
                while True:
                    sumi += 1
                    mini -= 1
                    if mini not in broken:
                        result += str(mini)
                        print(str(mini))
                        break
                    if mini not in broken:
                        result += str(sumi)
                        print(str(sumi))
                        break

        print(result)
        if int(result) < page:
            count = page - int(result)
        else:
            count = int(result) - page

        print(len(result)+count)


solution(158, [1, 9, 2, 5, 4])
