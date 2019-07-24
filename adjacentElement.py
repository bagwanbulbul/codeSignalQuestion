def adjacentElementsProduct(inputArray):
    i = 0
    new_list = []
    while i<len(inputArray)-1:
        a = inputArray[i]*inputArray[i+1]
        new_list.append(a)
        i =i+1
    j = 0
    max_number = new_list[j]
    while j<len(new_list):
        if new_list[j]>max_number:
            max_number = new_list[j]
        j = j+1
    return (max_number)
inputArray = [3,6,-2,-5,7,3]
print (adjacentElementsProduct(inputArray))

