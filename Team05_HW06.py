def bubblesort(mylist):
    for next_num in range(len(mylist)-1,0,-1):
        for i in range(next_num):
            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                
if __name__ == "__main__":
        
    mylist = [37,81,92,17,99,34,26,13,20,27]
    bubblesort(mylist)
    print(mylist)