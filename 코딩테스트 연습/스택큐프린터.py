def solution(priorities, location):
    result = []
    count = 0

    resultlist = list(range(1, len(priorities)+1))
    me = resultlist[location]

    while len(priorities) != 0:
        if priorities[0] < max(priorities):
            val = priorities.pop(0)
            priorities.append(val)
            resultlist.append(resultlist.pop(0))
        else:
            count += 1
            val = priorities.pop(0)
            result.append(val)
            if me == resultlist[0]:
                return count
            #print(val, resultlist[0], count)
            resultlist.pop(0)
    # return len(result[:leng-location-count])+1


solution([2, 1, 3, 2], 2)
#solution([2, 1, 3, 2, 1], 4)
#solution([1, 1, 9, 1, 1, 1], 0)
'''
9 1 1 1 1 2
2


3 2 2 1     c2 l2 r1        c2 l3 r2          c2 l1 r4      c2 l0 r3




2 1 3 2 1
1 3 2 1 2       2 : 1      c4 
3 2 1 2 1       0 : 3
2 1 2 1         
1 2 1
2 1 1 


2 1 3 2

1 3 2 2     2 -  1

3 2 2 1      2 - 2      0      4 - (4 - 0) = 0




3 2 1 4
내께 3번째야
그러면
2143 1432 4321 3번바껴 

len(result[:-2])에 내께 있어



1 1 9 1 1 1
1 9 1 1 1 1     0 - 1
9 1 1 1 1 1     0 - 2   -2 번째는 몇번째일까 6 - (6 + 2) = -2





def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''
