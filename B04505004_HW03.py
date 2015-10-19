def charFreqLister(inputSTR):
    n = len(inputSTR)
    frequency = {}
    letterlst = []
    for letter in inputSTR:
        from fractions import Fraction
        frequency[letter] = inputSTR.count(letter)/n
    for letter in frequency:
        letterlst.append((frequency[letter],letter))
    letterlst.sort(reverse=True)
    return letterlst


if __name__ == "__main__":
    testSTR01 = "The quick brown fox jumps over the lazy dog"
    result = charFreqLister(testSTR01)
    print(result)
    testSTR02 = "Jim quickly realized that the beautiful gowns are expensive"
    result = charFreqLister(testSTR02)
    print(result)