def solution(encrypted_text, key, rotation):
    if rotation > len(encrypted_text):
        rotation %= len(encrypted_text)
    encrypted = list(encrypted_text)
    result1 = ""
    if rotation < 0:
        rotation *= -1
        for i in range(rotation):
            rshift(encrypted)
    else:
        for i in range(rotation):
            shift(encrypted)

    keyed = list(key)
    for idx, val in enumerate(keyed):
        keyed[idx] = ord(val) - 96

    for idx, val in enumerate(encrypted):
        result_str = ord(val) - keyed[idx]
        if result_str < 97:
            result_str += 26
        else:
            result_str += 0
        result1 += chr(result_str)
    print(result1)
    return result1


def shift(arrays):
    temp = arrays[0]
    for i in range(1, len(arrays)):
        arrays[i-1] = arrays[i]
    arrays[len(arrays) - 1] = temp


def rshift(arrays):
    temp = arrays[len(arrays) - 1]
    for i in range(len(arrays)-1, 0, -1):
        arrays[i] = arrays[i-1]
    arrays[0] = temp


solution("qyyigoptvfb", "abcdefghijk", 14)
# 암호화된 놈에서 앞으로 회전 수 만큼 옮기고
# key의 값들을 숫자로 바꿔서 더하기 이때 1~26 이고
# 끝
'''
    for i in encrypted:
        result1 += i
    print(result1)
'''
