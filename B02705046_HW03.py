#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def charFreqLister(STR):
    result = []
    for i in range(0, len(STR)):
        c = False
        for j in range(0, len(result)):
            if result[j][0] == STR[i]:
                co = result[j][1] + 1
                result[j] = (STR[i], co)
                c = True
        if c == False:
            result.append((STR[i], 1))
    return result
if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)