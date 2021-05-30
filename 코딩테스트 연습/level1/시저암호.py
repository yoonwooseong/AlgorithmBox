def solution(s, n):
    result = ""
    for i in list(s):
        if i == " ":
            i = i
        else:
            if ord(i) >= 65 and ord(i) <= 90:
                if ord(i)+n > 90:
                    i = chr(ord(i)+n-26)
                else:
                    i = chr(ord(i)+n)
            if ord(i) >= 97 and ord(i) <= 122:
                if ord(i)+n > 122:
                    i = chr(ord(i)+n-26)
                else:
                    i = chr(ord(i)+n)
        result += i

    return result


'''
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
'''
