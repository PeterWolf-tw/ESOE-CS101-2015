#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#針對一個class Friends
#定義names 和 connected
#舉例如主程式後
#特別注意:在class裡{"a", "b"}和{"b", "a"}並無不同
# names 是舉出所有出現在Friends裡的"名字",不重複
# connected(a) 是舉出所有在Friends裡 和a有關的名字 
class Friends:
    def __init__(self, connections):
        
    
    
    def names(self):

        

    def connected(self, connections):
        
        



if __name__ == '__main__':
    
    friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
    friends2 = Friends(({"1", "2"}, {"2", "4"}, {"1", "3"}))
    
    
    
    # friends.names() == {"a", "b", "c"}, "Names"
    # friends.connected("d") == set(), "Non connected name"
    # friends.connected("a") == {"b", "c"}, "Connected name"
    # friends2.names() == {"1", "2", "3", "4"}
    # friends2.connected("1") == {"2", "3"}
