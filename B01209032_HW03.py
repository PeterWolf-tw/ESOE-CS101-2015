def charFreqLister(inputSTR):
    resultLIST = []
    p = len(inputSTR)

    for q in inputSTR:
        t = inputSTR.count(i)    
        if (q, t/p) not in resultLIST:
            resultLIST.append(q, t/p)
            resultLIST.sort(reverse = True)

    return resultLIST

if "_name_" == "_main_":
    print(charFreqLister(input("Plz! Type something!")))
