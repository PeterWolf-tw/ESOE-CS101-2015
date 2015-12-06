#condition00 not condition01
def condNOT(inputSTR_X):
    outputSTR = ""
    for i in inputSTR_X:
        if i == "0":
            outputSTR = outputSTR + "1"
        else:
            outputSTR = outputSTR + "0"
    return outputSTR

def chklen(inputSTR_X, inputSTR_Y):
    if len(inputSTR_X)!=len(inputSTR_Y):
        if len(inputSTR_X)>len(inputSTR_Y):
            L=len(inputSTR_X)-len(inputSTR_Y)
            for i in range(L):
                inputSTR_Y="0"+inputSTR_Y
        elif len(inputSTR_X)<len(inputSTR_Y):
            L=len(inputSTR_Y)-len(inputSTR_X)
            for i in range(L):
                inputSTR_X="0"+inputSTR_X
    return inputSTR_X, inputSTR_Y


#condition00 and condition02
def condAND(inputSTR_X, inputSTR_Y):
    inputSTR_X,inputSTR_Y=chklen(inputSTR_X, inputSTR_Y)
    outputSTR = ""
    print("x=",inputSTR_X," y= ",inputSTR_Y)
    for i,j in zip(inputSTR_X,inputSTR_Y):
        if i=="1" and j=="1":
            outputSTR+="1"
        else:
            outputSTR+="0"
    return outputSTR

#condition00 or condition03
def condOR(inputSTR_X, inputSTR_Y):
    inputSTR_X,inputSTR_Y=chklen(inputSTR_X, inputSTR_Y)
    outputSTR=""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i =="0" and j == "0":
            outputSTR+="0"
        else:
            outputSTR+="1"
    return outputSTR

#condition00 xor condition04
def conXOR(inputSTR_X, inputSTR_Y):
    inputSTR_X,inputSTR_Y=chklen(inputSTR_X, inputSTR_Y)
    outputSTR=""
    for i,j in zip(inputSTR_X, inputSTR_Y):
        if i == j :
           outputSTR +="1" #每次縮排空四格。這行少了一格。
        else :
           outputSTR +="0" #每次縮排空四格。這行少了一格。
    return outputSTR



def hex2Bin(hexSTR):
    '''
    16 進位表示式轉為 2 進位表示式
    '''
    return bin(int(hexSTR, 16))[2:]


if __name__== "__main__":
    while(1):
       # condition00X = "010111001010100001100011"
       # condition00Y = "010000110001011100101001"

        #condition02 = condAND(condition00X,condition00Y)
        #print("AND=",condition02)

       # condition01 = condNOT(condition00X)
       # print("NOT=",condition01)
       # condition03 = condOR(condition00X,condition00Y)
       # print("OR=",condition03)
        #condition04 = conXOR(condition00X,condition00Y)
        #print("XOR=",condition04)

        #可利用 hex2Bin() 函式計算十六進位表示式 "99" 的二進位表式：(範例如下)
        b = hex2Bin("99")

        CHK=input("Select a mode: 1.Binary 2.Heximal\n")
        if CHK=="1":
            num1=input("Input yout first number\n")
            num2=input("Input yout second number\n")
        elif CHK=="2":
            n1=input("Input yout first number\n")
            num1=hex2Bin(n1)
            n2=input("Input yout second number\n")
            num2=hex2Bin(n2)


        print("Select a function 1.NOT 2.AND 3.OR 4.XOR \n")
        a=input()
        if a=="1":
            condition01 = condNOT(num1)
            print("NOT=",condition01)
        elif a=="2":
            condition02 = condAND(num1,num2)
            print("AND=",condition02)
        elif a=="3":
            condition03 = condOR(num1,num2)
            print("OR=",condition03)
        elif a=="4":
            condition04 = conXOR(num1,num2)
            print("XOR=",condition04)

    print("Ans:") #每次縮排空四格。這行多了兩格。
    Ch4P4_3a = "10011001"
    Ch4P4_3b = "11111111"
    Ch4P4_3c = "10011001"
    Ch4P4_3d = "11111111"
    print("========")
    Ch4P4_4a = "01100110"
    Ch4P4_4b = "11111111"
    Ch4P4_4c = "10001"
    Ch4P4_4d = "10111011"
    print("========")
    Ch4P4_13a = "0000010010100000 = 1184"
    Ch4P4_13b = "1111110010100010 = -862"
    Ch4P4_13c = "0000001101011110 = 862"
    Ch4P4_13d = "1111101101100000 = -1184"
    print("========")
    Ch4P4_15a = "10001001 = -119 => overflow"
    Ch4P4_15b = "10110111 = -73"
    Ch4P4_15c = "01001001 = 73"
    Ch4P4_15d = "01110111 = 119 => overflow"
    print("========")
    Ch4P4_16a = "0F51"
    Ch4P4_16b = "0F2A"
    Ch4P4_16c = "8012"
    Ch4P4_16d = "7F51"
