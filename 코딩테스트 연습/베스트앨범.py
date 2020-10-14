def solution(genres, plays):
    dic = {}
    maxnum = max(plays)
    maxstr = ""
    maxidx = 0
    count = 1
    maxlist = []
    maxname = list(range(len(set(genres))))
    resultlist = []
    
    for i in range(len(genres)):
        hashdic = {}
        if genres[i] in dic.keys():
            hashdic = dic[genres[i]]
        hashdic[i] = plays[i]
        dic[genres[i]] = hashdic
    
    for i in dic.keys():
        dic[i]["max"] = max(dic[i].values())
        maxlist.append(dic[i]["max"])
        '''
        print(dic[i]["max"])
        for j in dic[i].keys():
            # j = 1, 4
            if maxnum == dic[i][j]:
                maxstr = i
                maxidx = j
        '''
    maxlist.sort(reverse=True)
    for i in dic.keys():
        for idx, val in enumerate(maxlist):
            if dic[i]['max'] == val:
                dic[i]['rank'] = idx+1
                maxname[idx] = i
                


            
    print(maxstr, maxnum, maxidx)
    print(maxname)

    for i, v in enumerate(maxname):
        hi = sorted(dic[v].items(), key=lambda x: x[1], reverse=True)
        resultlist.append(hi[0][0])
        resultlist.append(hi[2][0])
        if i == 1:
            break

    print(resultlist)
    print(dic)
    return resultlist

genres = ["classic", "pop", "classic", "classic", "pop", "jazz"]
plays = [500, 600, 150, 800, 2500, 900]	
solution(genres, plays)

 
        