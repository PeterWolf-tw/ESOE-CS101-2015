#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from itertools import chain


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)



    def names(self):
        return set(chain(*self.connections))

    def connected(self, name):
        neighbors = []
        [neighbors.extend(list(i)) for i in self.connections if name in i]
        neighbors = set(neighbors)
        if name in set(neighbors):
            neighbors.remove(name)
        return neighbors


if __name__ == '__main__':
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    print( letter_friends.names())
    print( letter_friends.connected("d") )
    print( letter_friends.connected("a") )
#=====Team03=====
#Team01:Fail
#Team02:Fail
#Team04:Pass
#Team05:Fail
#Team06:Pass
#Team07:Fail
#Team08:Fail
#Team09:Pass
#Team10:??
#Team11:Pass
#Team12:Pass
#Team13:Pass
#Team14:Fail