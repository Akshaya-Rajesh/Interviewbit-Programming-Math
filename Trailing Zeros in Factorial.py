#Given an integer n, return the number of trailing zeroes in n!

class Solution:
    # @param A : integer
    # @return an integer
    import math 
    
    def trailingZeroes(self, A):
        count=0
        
        #Trailing 0s in n! = Count of 5s in prime factors of n!
        #                  = floor(n/5) + floor(n/25) + floor(n/125) + ....
        
        i=5
        while (A/i>=1): 
            count += int(A/i) 
            i *= 5
            
        return int(count)
