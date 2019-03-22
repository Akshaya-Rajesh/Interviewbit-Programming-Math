class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        upperLimit = int(A**0.5)
        if(A<=1):
            return 0
        for i in xrange(2, upperLimit + 1):
            if(A % i == 0):
                return 0
        return 1
