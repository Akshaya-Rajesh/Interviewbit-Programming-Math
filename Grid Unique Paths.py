class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    import math
    
    def uniquePaths(self, A, B):
        fact=math.factorial
        
        # m + n - 2 steps in total.  You have to take (m - 1) steps going down and (n-1) steps going right.
        # So we need to find out the number of strings of length m + n - 2 which have exactly m - 1 zeroes and n - 1 ones.
        # So, the answer becomes Choose(m+n-2, n - 1).
        
        return(int(fact(A+B-2)/(fact(B-1)*fact(A-1))))
