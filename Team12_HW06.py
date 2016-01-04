def BubbleSorting(intlist):
    for Number in range(len(intlist)-1,0,-1):
        for i in range(Number):
            if intlist[i] < intlist[i+1]:
                n = intlist[i]
                intlist[i] = intlist[i+1]
                intlist[i+1] = n

intlist = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
BubbleSorting(intlist)
print(intlist)
