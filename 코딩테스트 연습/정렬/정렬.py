def solution(array, commands):
    answer = []
    for i in commands:
        sublist = array[i[0]-1:i[1]]
        sublist.sort()
        answer.append(sublist[i[2]-1])
    return answer


'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
