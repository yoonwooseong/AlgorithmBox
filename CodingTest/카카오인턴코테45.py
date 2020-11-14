import itertools
print(list(itertools.combinations(range(6), 2)))
numberOfAttributes = int(input())
supportThreshold = float(input())
numberOfRows = int(input())
data = input().split(" ")


print(numberOfAttributes)
print(supportThreshold)
print(numberOfRows)
print(data)

total_data = []
for i in data:
    dic1 = {}
    listA = data.split(",")
    listB = listA.split("=")
    dic1[listB[0]] = listB[1]

print(total_data)
