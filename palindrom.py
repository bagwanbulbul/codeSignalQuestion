def checkPalindrome(inputString):
    i = 0
    j = -1
    while i<len(inputString):
        if inputString[i] == inputString[j]:
            a = True
            j = j-1
            i = i+1
        else:
            return False
    return a
checkPalindrome("aaabaaaa")
