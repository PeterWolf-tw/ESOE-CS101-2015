#�Ĥ@�D�O���O�o�˥����A�|���H�Ф@�U�Aby jeffntu
if __name__ == '__main__':
    n = 0
    p = raw_input('input a bin number:\n')
    for i in range(len(p)):
        n = n * 2 + ord(p[i]) - ord('0')
    print n
