def solution(genres, plays):
    dic = {}
    dic2 = {}
    resultlist = []
    
    for i in range(len(genres)):
        hashdic = {}
        if genres[i] in dic.keys():
            hashdic = dic[genres[i]]
        hashdic[i] = plays[i]
        dic[genres[i]] = hashdic
    
    for i in dic:
        dic2[i] = sum(j for j in dic[i].values())

    hi = sorted(dic2.items(), key=lambda x: x[1], reverse=True)
    for i, v in enumerate(hi):
        hi2 = sorted(dic[v[0]].items(), key=lambda x: x[1], reverse=True)
        resultlist.append(hi2[0][0])
        try:
            resultlist.append(hi2[1][0])
        except:
            print()
    return resultlist


genres = ["classic", "pop", "classic", "classic", "pop", "jazz"]
plays = [500, 600, 200, 200, 2500, 900]	
solution(genres, plays)

 
        