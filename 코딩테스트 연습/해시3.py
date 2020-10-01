def solution(clothes):
    hashmap = {}
    count = 1
    for val in clothes:
        hashlist = [""]
        if val[1] in hashmap.keys():
            hashlist = hashmap[val[1]]
        hashlist.append(val[0])
        hashmap[val[1]] = hashlist
    
    for idx in hashmap.values():
        count *= len(idx)
    return count-1
    
solution([["yellow_hat", "face2"], ["blue_sunglasses", "fac2e"], ["green_turban", "f2ace"]])

'''
1
2
3
4
5
6
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
'''