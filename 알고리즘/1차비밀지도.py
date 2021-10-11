def solution(n, arr1, arr2):
    arr3 = []
    for idx, val in enumerate(arr1):
        arr3.append(format(val | arr2[idx], 'b').replace(
            "1", "#").replace("0", " ").rjust(n, " "))
    return arr3


solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
