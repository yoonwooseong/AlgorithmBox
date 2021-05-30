
def editDistance(source, target):
    # Write your code here
    listA = []
    ex = ord(source[0])
    for i in source[1:]:
        listA.append(ex - ord(i))

    listB = []
    ex2 = ord(target[0])
    for i in target[1:]:
        listB.append(ex2 - ord(i))

    count = 0
    maxnum = qlry(listA, listB)
    for i in range(len(listA)):
        listB.append(listB.pop(0))
        if maxnum < qlry(listA, listB):
            maxnum = qlry(listA, listB)

    print(len(source) - maxnum)

    for i in zip(listA, listB):
        if i[0] != i[1]:
            count += 2

    print(count)


def qlry(a, b):
    count = 0
    for i in zip(a, b):
        if i[0] == i[1]:
            count += 1
    print(count)
    return count


editDistance("mqfsnmygrquczhymvkurxfelpeagkisearktnjrcapbuuawnmcrgsfsnusuprtnnzbuvtoemgiohvicsnkqhbgoomupuvjmfzpqp",
             "yelitmysnjcfgvvvezaprgaonzkofyqqhfmxseezencanocepyzxocwivnkbjrhcehqlcwsagrfookhiwsrjguzonapppyyodlqx")
