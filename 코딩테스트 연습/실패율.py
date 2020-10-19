def solution(N, stages):
    score = []
    chance = []
    avg = {}
    result = []
    for i in range(N):
        score.append(0)
        chance.append(0)
        for j in stages:
            if i <= j-1:
                chance[i] += 1
            if j == i+2:
                continue
            if i == j-1:
                score[j-1] += 1

    for idx, val in enumerate(score):
        if chance[idx] == 0:
            avg[idx+1] = 0
        else:
            avg[idx+1] = val/chance[idx]

    for i in sorted(avg.items(), key=lambda x: x[1], reverse=True):
        result.append(i[0])
    return result


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
