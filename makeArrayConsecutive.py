def makeArrayConsecutive2(statues):
    i = 0
    minimum = statues[i]
    maximum_num = statues[i]
    while i<len(statues):
        if minimum>statues[i]:
            minimum = statues[i]
        i = i+1
    i = 0
    while i<len(statues):
        if maximum_num<statues[i]:
            maximum_num = statues[i]
        i = i+1
        count = 0
        j = 0
    while j<maximum_num:
        if j not in statues and minimum<j:
            count = count +1
        j = j+1
    return count
statues = [6,2,3,8]
print (makeArrayConsecutive2(statues))

    



