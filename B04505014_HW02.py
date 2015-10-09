#第一題是不是這樣打ㄚ，會的人教一下，by jeffntu
if __name__ == '__main__':
    n = 0
    p = raw_input('input a bin number:\n')
    for i in range(len(p)):
        n = n * 2 + ord(p[i]) - ord('0')
    print n
