#Python3 program to check if a given number can be expressed as power

class Solution:
    # @param A : integer
    # @return an integer
    
    import math
    
    def isPower(self, A):
    # Returns 1 if n can be written as x ^ y 
        if(A<=1):
            return 1
        for i in range(2,int(math.sqrt(A))+1):
            p=i
            while(p<=A):
                p*=i
                if(p==A):
                   return 1
        return 0
