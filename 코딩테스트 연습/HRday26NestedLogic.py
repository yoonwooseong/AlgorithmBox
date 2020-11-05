# Enter your code here. Read input from STDIN. Print output to STDOUT
aD, aM, aY = input().split(" ")
eD, eM, eY = input().split(" ")
result = 0
if int(aY) > int(eY):
    result = 10000
elif int(aM) > int(eM) and int(aY) >= int(eY):
    result = 500*(int(aM)-int(eM))
elif int(aD) > int(eD) and int(aM) >= int(eM) and int(aY) >= int(eY):
    result = 15*(int(aD)-int(eD))
else:
    result = 0


print(result)
