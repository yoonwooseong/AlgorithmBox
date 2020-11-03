import queue


def solution(board, moves):
    # 배열을 세로로 재정의한 후 큐로 0이 아닌 가장 먼저 들어와 있는
    # 놈을 가져와서 바구니에 저장
    # 저장 시 바구니 마지막값이 같으면 지우면서 카운트 +2
    queuelist = []
    bounds = [0]
    removecount = 0
    for i in range(len(board)):
        q = queue.Queue()
        queuelist.append(q)

    for i in range(len(board)):
        for j in range(len(board[i])):
            queuelist[j].put(board[i][j])

    for i in moves:
        while True:
            if queuelist[i-1].empty() == True:
                break
            else:
                doll = queuelist[i-1].get()
                print(doll)
                if doll != 0:

                    bounds.append(doll)
                    if bounds[-1] == bounds[-2]:
                        bounds.pop()
                        bounds.pop()
                        removecount += 2
                        while bounds[-1] == bounds[-2]:
                            bounds.pop()
                            bounds.pop()
                            removecount += 2
                    break
    print(removecount)
    return removecount


# 4 3 1 1 3 2 4

solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
         4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]	)
