import heapq


def solution(d, budget):
    sumbudget = 0
    count = 0
    heapq.heapify(d)

    while True:
        if len(d) != 0:
            onebudget = heapq.heappop(d)
            if onebudget+sumbudget <= budget:
                sumbudget += onebudget
                count += 1
            else:
                return count
        else:
            return count


solution([2, 2, 3, 3], 10)
