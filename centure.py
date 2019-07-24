def centuryFromYear(year):
    devide = year/100
    if year%100!=0:
        devide = devide+1
        return int(devide)
    else:
        return devide
print (centuryFromYear(2000))

