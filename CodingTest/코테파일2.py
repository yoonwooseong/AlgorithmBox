def solution(N, coffee_times):
    make_list = []
    result_list = []
    minRe = 0
    for i in range(int(len(coffee_times)/N)+1):
        for j in range(N):
            try:
                make_list.append(coffee_times[N*i+j] + minRe)

            except:
                print("")
        print("커피만드누ㅡㄴ중 : " + str(make_list))
        print("최솟값 인덱스 : " + str(make_list.index(min(make_list))))
        print("최솟값 : " + str(make_list[make_list.index(min(make_list))]))
        minRe += int(make_list[make_list.index(min(make_list))])
    print(make_list)

    for i in range(len(make_list)):

        result_list.append(1+int(make_list.index(min(make_list))))
        make_list[make_list.index(min(make_list))] = 500000

    print(result_list)


solution(1, [100, 1, 50, 1, 1])
