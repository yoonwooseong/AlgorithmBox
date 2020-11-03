def solution(n):
    distinguish = [False, False]+[True]*(n-1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if distinguish[i] == True:
            for j in range(i*2, n+1, i):
                distinguish[j] = False
    print(distinguish)
    return distinguish.count(True)
    # return [i for i in range(2, n) if distinguish[i] == True]


solution(5)
'''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
'''
