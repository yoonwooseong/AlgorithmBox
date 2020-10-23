def solution(arr1, arr2):
    for idx, val in enumerate(arr2):
        for idx2, val2 in enumerate(val):
            arr1[idx][idx2] += val2
    return arr1


'''
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
'''
