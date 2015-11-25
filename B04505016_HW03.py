def charFreqLister(inputSTR):
    resultLIST =[]
    freq = []
    
    
    for i in inputSTR:
        c = inputSTR.count(i)
        if (i,c/len(inputSTR)) not in resultLIST:
            resultLIST.append(i,c/len(inputSTR))
            resultLIST.sort(key = lambda x : x[1], reverse=True)
            
            return resultLIST


if "_name_" == "_main_":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR)
    print(result)    
    