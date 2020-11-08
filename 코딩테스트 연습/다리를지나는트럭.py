from queue import Queue


def solution(bridge_length, weight, truck_weights):
    q = Queue()
    for i in truck_weights:
        q.put(i)

    print(q.get(0))
    print(q.qsize())


solution(2, 10, [7, 4, 5, 6])
