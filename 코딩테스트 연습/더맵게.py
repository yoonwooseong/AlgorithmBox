import heapq


def solution(scoville, K):
    count = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    # heapq.heapify(scoville)

    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + heapq.heappop(h)*2)
        except:
            return -1
        count += 1

    return count
