removeNum = 0
count = 0


def solution(s):
    global removeNum
    numbers = remov(s)
    while True:
        if numbers == 1:
            return [count, removeNum]
        else:
            numbers = remov(numbers)


def remov(s):
    global removeNum
    global count
    count += 1
    num = str(s).count("1")
    removeNum += (len(str(s)) - num)
    bnum = int(str(bin(num))[2:])
    #print(removeNum, bnum)
    return bnum


solution(110010101001)
