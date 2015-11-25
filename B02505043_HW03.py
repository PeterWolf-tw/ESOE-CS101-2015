#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def charfreqlister(str):
    len_str = len(str)
    
    result = []
    for c in str:
        is_inside = False
        for element in result:
            if element[1] == c:
                element[0] += 1
                is_inside = True
                break
        if not is_inside:
            result.append([1, c])
            
    for element in result:
        element[0] /= len_str

    return result

if __name__ == "__main__":
    print(charfreqlister("Iverson"))
