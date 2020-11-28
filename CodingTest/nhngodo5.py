def solution(votes):
    count = 0
    if len(votes) == 1:
        return 0
    if max(votes) == min(votes):
        return 1
    while True:
        maxidx = votes.index(max(votes))
        maxnum = max(votes)

        print(maxidx, maxnum)
        if 0 != maxidx:
            votes[maxidx] -= 1
            votes[0] += 1
            count += 1
        else:
            if votes.count(maxnum) != 1:
                count += 1
            break

    print(votes, count)


solution([1])
