def bin2int(N):
    n = str(N)
    an = 0
    p = 0
    while p < len(n):
        if n[p] == '1':
            an += 2 ** (len(n) - 1 - p)
        p += 1
    return an