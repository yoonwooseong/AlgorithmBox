import queue


def solution(progresses, speeds):
    j = 0
    result = []

    while len(progresses):
        count = 0
        while progresses[0] + speeds[0]*j < 100:
            j += 1
            if progresses[0] + speeds[0]*j >= 100:
                break

        while len(progresses):
            if progresses[0] + speeds[0]*j >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        result.append(count)
    return result
# 만약 100이상이면 계속 빼기
    '''
    q = queue.Queue()
    result = []
    count = 0
    for v1, v2 in zip(progresses, speeds):
        q.put([v1, v2])

    while q.empty() == False:
        lists = q.get()
        i = 0
        while i >= (100 - lists[0])/lists[1]:
            i+=1
        if 
    '''


solution([93, 30, 55], [1, 30, 5])
