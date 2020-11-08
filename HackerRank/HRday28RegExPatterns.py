#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    db = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID.find("@gmail.com") != -1:
            db.append(firstName)

    for i in sorted(db):
        print(i)

'''
import re

arr = []

n = int(input())

for i in range(n):
    data = str(input()).split(" ")
    name = data[0]
    email = data[1]

    if re.search(".+@gmail\.com$", email):
        arr.append(name)

arr.sort()

for name in arr:
    print(name)
'''
