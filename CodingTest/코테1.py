def solution(n, customers):
    startKO = []
    endKO = []
    count = []
    customers.sort()

    for i in range(n):
        startKO.append(customers[i][:14])
        # 끝나는 시간 계산
        sec = int(customers[i][12:14])+int(customers[i][15:])

        if sec < 60:
            formatsec = "%02d" % sec
            endtime = customers[i][:12]+str(formatsec)
        else:
            # 만약 오류나면 여기 60분 됬을때도 조건
            formatsec = "%02d" % (sec % 60)
            endtime = customers[i][:10] + \
                str(int(customers[i][10:11])+1)+":"+str(formatsec)
        endKO.append(endtime)
        count.append(1)

    for i in range(len(customers)-n):
        currenttime = customers[i+n][:14]
        print(currenttime)
    print(startKO)
    print(endKO)
    print(count)
    print(customers)
    answer = 0
    return answer


solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24",
             "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"])
