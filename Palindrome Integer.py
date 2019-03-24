class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, n):
        divisor = 1
        while (n / divisor >= 10): 
            divisor *= 10
        while (n != 0):
            leading = n // divisor
            trailing = n % 10
            if (leading != trailing):  
                return(0)
            n = (n % divisor)//10
            divisor = divisor/100
        return(1)
