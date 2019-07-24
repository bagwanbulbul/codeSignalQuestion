def allLongestStrings(inputArray):
        i = 0
        count=0
        new=[]
        while i<len(inputArray):
                max = len(inputArray[i])
                if count<max:
                        count=max
                i=i+1
        b=0
        while b<len(inputArray):
                if len(inputArray[b])==count:
                        new.append(inputArray[b])
                b=b+1
        return new
inputArray = ["aba","aa","ad","vcd","aba"]
allLongestStrings(inputArray)
        


