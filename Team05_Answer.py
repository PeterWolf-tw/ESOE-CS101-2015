def LLS(xdata,ydata):
    # y = ax + b
    c = 0
    for i in range(len(xdata)):
        c = c + xdata[i]**2
    d = 0
    for k in range(len(xdata)):
        d = d + xdata[k]
    e=d
    f = len(xdata)
    detm = c*f-d*e
    g = 0
    for j in range(len(xdata)):
        g = g + xdata[j]*ydata[j]
    h = 0
    for l in range(len(ydata)):
        h = h + ydata[l]    
    a = (f*g - h*d)/detm
    b = (c*h - e*g)/detm
    print(c,' ',d,' ',e,' ',f,' ',g,' ',h)
    print("y = ",a,"x+",b)
if __name__ == "__main__":
    LLS([2,2.6,5.4,4.2,3.2,6.6,1.5,3.8], [3.4,4.8,6.2,5,4.2,6.5,4.6,5.3])


#======TEAM05======
'''
TEAM01:FAIL
TEAM02:FAIL
TEAM03:FAIL
TEAM04:FAIL(PLEASE FOLLOW INSTRUCTION)
TEAM06:FAIL
TEAM07:EXCELLENT PASS
TEAM08:FAIL
TEAM09:FAIL(int...)
TEAM10:N/A
TEAM11:PASS
TEAM12:FAIL
TEAM13:FAIL
TEAM14:FAIL
'''