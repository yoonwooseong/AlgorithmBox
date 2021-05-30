import json
import urllib.request

url2 = "https://jsonmock.hackerrank.com/api/iot_devices/search?status=running"
data2 = urllib.request.urlopen(url2).read()
total_page = json.loads(data2)['total_pages']
print(total_page)
count = 0
rospeed = 0

for num in range(1, total_page+1):
    url = "https://jsonmock.hackerrank.com/api/iot_devices/search?status=running&page=" + \
        str(num)
    data = urllib.request.urlopen(url).read()
    for i in range(len(json.loads(data)['data'])):
        try:
            if json.loads(data)['data'][i]['parent']['id'] == 7:
                count += 1
                rospeed += json.loads(
                    data)['data'][i]['operatingParams']['rotorSpeed']
        except:
            counts = 0

print(rospeed/count)

'''
#!/bin/python3

import math
import os
import random
import re
import sys


import json
import urllib.request
#
# Complete the 'avgRotorSpeed' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER parentId
#
def avgRotorSpeed(statusQuery, parentId):
    # Write your code here
    page_url = "https://jsonmock.hackerrank.com/api/iot_devices/search?status="+statusQuery
    pagedata = urllib.request.urlopen(page_url).read()
    total_page = json.loads(pagedata)['total_pages']
    count = 0
    rospeed = 0
    
    for num in range(1, total_page+1):
        url = "https://jsonmock.hackerrank.com/api/iot_devices/search?status="+statusQuery+"&page="+str(num)
        data = urllib.request.urlopen(url).read()
        for i in range(len(json.loads(data)['data'])):
            try:
                if json.loads(data)['data'][i]['parent']['id'] == parentId:
                    count += 1
                    rospeed += json.loads(data)['data'][i]['operatingParams']['rotorSpeed']
            except:
                counts = 0
    if count == 0:
        return 0
    return int(rospeed/count)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    statusQuery = input()

    parentId = int(input().strip())

    result = avgRotorSpeed(statusQuery, parentId)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
