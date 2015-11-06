#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from __future__ import division

def charFreqLister(inputSTR):
    a = len(inputSTR)
    freq = {}
    letterlist = []
    for letter in inputSTR:
        freq[letter] = inputSTR.count(letter)/a
    for letter in freq:
        letterlist.append((freq[letter],letter))
    letterlist.sort(reverse=True)
    return letterlist


if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)
