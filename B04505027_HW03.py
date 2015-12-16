def charFreqLister(inputSTR):
    
    
    resultLIST = [(inputSTR.count(x)/len(inputSTR),x) for x in set(inputSTR)]
    resultLIST.sort( key = lambda x : x[0], reverse=True)
     
    return resultLIST
    
if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)    
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)
