# coding:utf-8 

def int2bin(N):
    '''
    本函式將 int 整數轉為 bin 二進位制表示
    '''
    s=N
    tmpLIST = []
    while N > 0:
        remainder = int(N % 2)
        tmpLIST.append(remainder)
        N = (N - remainder) / 2
    tmpLIST.append(0)

    ans = ""
    for j in tmpLIST[::-1]: #將 tmpLIST 中的數字從尾至頭傳入 j
        ans = ans + str(j)
    print ("{0} 的二進位表示為 {1}.".format(s, ans))
    return None

def bin2int(N):
    number=int(N)
    length=len(N)
    n=0
    for i in range(length):
        n+=number%10*(2**i)
        number=int(number/10)
    print ("{0} 的二進位表示為 {1}.".format(N, n))
    return None

if __name__ == '__main__':
    intNumber = 100
    int2bin(intNumber)
    binNumber = "01100101"
    bin2int(binNumber)




