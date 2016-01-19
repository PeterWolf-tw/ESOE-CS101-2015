#!/usr/bin/env python 3
#-*- coding:utf-8 -*-


class Family:  
    def __init__(self, empid, name, lordid):  
        self.empid = empid  
        self.name = name  
        self.lordid = lordid  

def relationMSG(inputSTR_X,inputSTR_Y): 

    family_objects=[]
    family_objects.append( Family('100', 'Jon Snow', '200') )
    family_objects.append( Family('200', 'Robert Stark', '300') )
    family_objects.append( Family('300', 'Eddard Stark', '300') )
    family_objects.append( Family('400', 'Bran Stark', '300') )
    family_objects.append( Family('500', 'Tywin Lannister', '500') )
    family_objects.append( Family('600', 'Jamie Lannister', '500') )
    family_objects.append( Family('800', 'Ser Rodrik', '200') )
    family_objects.append( Family('900', 'Hodor', '400') )
    family_objects.append( Family('700', 'Rhaegar Targaryen', '000') )

    XSTR = inputSTR_X              
    XList = []                     
    XList.append(XSTR)
    print(XList)
    YSTR = inputSTR_Y              
    YList = []                    
    YList.append(YSTR)
    print(YList)
    swX = ""                         
    swY = ""                      
    Msg = ""
    
    for i in family_objects:
        if i.empid == XSTR:
            swX = "Y"               
            XList.append(i.lordid)
           
        if i.empid == YSTR:        
            swY = "Y"              
            YList.append(i.lordid)

    if swX == "" or swY == "":
        if swX == "":
            Msg = XSTR+"不在資料中,無法找出關係!"
        if swY == "":
            Msg = Msg+YSTR+"不在資料中,無法找出關係!"
    else:      
        swX = ""                      
        swY = ""                       
        for i in family_objects:
            if i.empid == str(XList[1]):        
                swX = "Y"
                XList.append(i.lordid)
           
            if i.empid == str(YList[1]):        
                swY = "Y"
                YList.append(i.lordid)
           
        print("This is XList=",XList)      
        print("This is YList=",YList)    

        if swX == "" or swY == "":
            if swX == "":
                Msg = XSTR+"的長官"+XList[1]+"不在資料中,資料有誤無法找出關係!"
            if swY == "":
                Msg = Msg+YSTR+"的長官"+YList[1]+"不在資料中,資料有誤無法找出關係!"
 
        elif XList[2] != YList[2]:        
            Msg = str(XList[0])+"和"+str(YList[0] )+"是敵人"

        else:                            
            if XList[0] == XList[1] == XList[2]:                
                Msg = str(XList[0])+"是"+str(YList[0] )+"的長官"

            elif YList[0] == YList[1] == YList[2]:              
                Msg = str(XList[0])+"是"+str(YList[0] )+"的部屬"

            else:                                               
                if XList[1] == YList[1]:                            
                    Msg = str(XList[0])+"和"+str(YList[0] )+"是平輩"      

                else:                                          
                    if XList[1] == YList[0]:                          
                        Msg = str(XList[0])+"是"+str(YList[0] )+"的部屬"   
                    elif YList[1] == XList[0]:                        
                        Msg = str(XList[0])+"是"+str(YList[0] )+"的長官"  
                    else:                                             
                        Msg = str(XList[0])+"和"+str(YList[0] )+"是平輩"    

    return Msg        

if __name__ == "__main__":
    strX = "100"
    strY = "600"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "200"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "800"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "900"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "400"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "300"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "200"
    strY = "500"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "200"
    strY = "400"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "200"
    strY = "800"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "200"
    strY = "900"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "200"
    strY = "300"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "100"
    strY = "700"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "900"
    strY = "400"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "900"
    strY = "200"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "900"
    strY = "300"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "400"
    strY = "800"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "400"
    strY = "200"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "400"
    strY = "900"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "400"
    strY = "300"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "400"
    strY = "800"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "600"
    strY = "400"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "500"
    strY = "600"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "300"
    strY = "700"
    printMSG = relationMSG(strX,strY)
    print(printMSG)

    strX = "000"
    strY = "100"
    printMSG = relationMSG(strX,strY)
    print(printMSG)
    
    
    
    
    
    
    
##############Team13##################
#Team01:Fail(未作答)
#Team02:Fail(未作答)
#Team03:Fail(未作答)
#Team04:Fail(未作答)
#Team05:Pass
#Team06:Fail(未作答)
#Team07:Fail(未作答)
#Team08:Fail(未作答)
#Team09:Fail(與Rhaegar Targaryen的關係有誤)
#Team10:由助教協助
#Team11:Fail(與Rhaegar Targaryen的關係有誤)
#Team12:Fail(與Rhaegar Targaryen的關係有誤)
#Team14:Fail(未作答)
