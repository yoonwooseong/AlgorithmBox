#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)
'''
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        maxnum = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                bitand = i & j
                if k > bitand > maxnum:
                    maxnum = bitand

        print(maxnum)
'''
'''
# 구글링해서 k가 홀수일때와 짝수일때의 비트연산자 or(|)를 사용해서 제출하는 방법을 알아냄. 
# 정확히 이해는 안가는 부분이라 따로 학습이 필요할듯
if (k|(k-1)) <= n:
    print(k-1)  
else:
    print(k-2)
'''
