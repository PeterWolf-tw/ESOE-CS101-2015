Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.

def BubbleSort(LIST):
   for j in range(len(LIST)-1,0,-1):
       for i in range(j):
            if LIST[i] < LIST[i+1]:
                n = LIST[i]
                LIST[i] = LIST[i+1]
                LIST[i+1] = n


if __name__ == '__main__': 
   LIST = [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
   BubbleSort(LIST)
   print(LIST)
